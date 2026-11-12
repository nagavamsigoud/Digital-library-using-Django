from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from store.models import Book
from .cart import Cart

@require_POST
def cart_add(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Book, pk=bookid)
    is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"
    try:
        cart.add(book)
        if is_ajax:
            return JsonResponse({"ok": True, "cart_count": len(cart)})
        messages.success(request, "Book added to your cart.")
    except ValueError as exc:
        if is_ajax:
            return JsonResponse({"ok": False, "error": str(exc)}, status=400)
        messages.error(request, str(exc))
    return redirect("cart:cart_details")

@require_POST
def cart_update(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Book, pk=bookid)
    try:
        cart.update(book, request.POST.get("quantity", ""))
        messages.success(request, "Cart quantity updated.")
    except (ValueError, TypeError, KeyError) as exc:
        messages.error(request, str(exc))
    return redirect("cart:cart_details")

@require_POST
def cart_remove(request, bookid):
    cart = Cart(request)
    cart.remove(get_object_or_404(Book, pk=bookid))
    return redirect("cart:cart_details")

def total_cart(request):
    return render(request, "cart/totalcart.html")

def cart_summary(request):
    return render(request, "cart/summary.html")

def cart_details(request):
    return render(request, "cart/cart.html", {"cart": Cart(request)})
