from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from cart.cart import Cart
from store.models import Book
from .forms import OrderCreateForm
from .models import Order, OrderItem
from .pdfcreator import render_pdf_bytes

@login_required
@require_http_methods(["GET", "POST"])
def order_create(request):
    cart = Cart(request)
    if not len(cart):
        messages.info(request, "Your cart is empty.")
        return redirect("store:books")
    form = OrderCreateForm(request.POST or None, initial={"name": request.user.first_name, "email": request.user.email})
    if request.method == "POST" and form.is_valid():
        try:
            with transaction.atomic():
                locked_items = []
                subtotal = Decimal("0.00")
                for book_id, cart_item in cart.cart.items():
                    book = Book.objects.select_for_update().get(pk=book_id)
                    quantity = int(cart_item["quantity"])
                    if quantity < 1 or quantity > 10 or quantity > book.stock:
                        raise ValueError(f"Not enough stock for {book.name}.")
                    subtotal += Decimal(str(book.price)) * quantity
                    locked_items.append((book, quantity))
                order = form.save(commit=False)
                order.customer = request.user
                order.payable = subtotal + settings.SHIPPING_FEE
                order.totalbook = sum(quantity for _, quantity in locked_items)
                order.save()
                for book, quantity in locked_items:
                    OrderItem.objects.create(order=order, book=book, price=book.price, quantity=quantity)
                    book.stock -= quantity
                    book.save(update_fields=["stock", "updated"])
            cart.clear()
            return render(request, "order/successfull.html", {"order": order})
        except (ValueError, Book.DoesNotExist) as exc:
            messages.error(request, str(exc))
    return render(request, "order/order.html", {"form": form, "cart": cart})

@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user).order_by("-created")
    return render(request, "order/list.html", {"myorder": orders})

@login_required
def order_details(request, id):
    order = get_object_or_404(Order, pk=id, customer=request.user)
    return render(request, "order/details.html", {"o_summary": order, "o_item": order.items.select_related("book")})

@method_decorator(login_required, name="dispatch")
class OrderPDFView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, pk=id, customer=request.user)
        pdf_bytes = render_pdf_bytes("order/pdf.html", {"order": order})
        if pdf_bytes is None:
            return HttpResponse("Unable to generate invoice.", status=500)
        response = HttpResponse(pdf_bytes, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="order-{order.pk}.pdf"'
        return response

