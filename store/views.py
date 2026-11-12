from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import RegistrationForm, ReviewForm
from .models import Book, Review, Slider, Writer


@ensure_csrf_cookie
def index(request):
    return render(request, "store/index.html", {
        "newbooks": Book.objects.order_by("-created")[:15],
        "slide": Slider.objects.order_by("-created")[:3],
    })


def signin(request):
    if request.user.is_authenticated:
        return redirect("store:index")
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("user", ""), password=request.POST.get("pass", ""))
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", "")
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
                return redirect(next_url)
            return redirect("store:index")
        messages.error(request, "Username or password is incorrect.")
    return render(request, "store/login.html")


@require_POST
def signout(request):
    logout(request)
    return redirect("store:index")


def registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your account has been created. Please sign in.")
        return redirect("store:signin")
    return render(request, "store/signup.html", {"form": form})


@ensure_csrf_cookie
def get_book(request, id):
    book = get_object_or_404(Book, pk=id)
    form = ReviewForm(request.POST or None)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please sign in before submitting a review.")
            return redirect("store:signin")
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.book = book
            review.save()
            Book.objects.filter(pk=book.pk).update(totalreview=F("totalreview") + 1, totalrating=F("totalrating") + review.review_star)
            messages.success(request, "Your review has been added.")
            return redirect("store:book", id=book.pk)
    reviews = Review.objects.filter(book=book).order_by("-created")
    context = {"book": book, "rbooks": Book.objects.filter(category=book.category).exclude(pk=book.pk),
               "form": form, "rreview": Paginator(reviews, 4).get_page(request.GET.get("page"))}
    return render(request, "store/book.html", context)


@ensure_csrf_cookie
def get_books(request):
    books = Book.objects.all().order_by("-created")
    return render(request, "store/category.html", {"book": Paginator(books, 10).get_page(request.GET.get("page"))})


@ensure_csrf_cookie
def get_book_category(request, id):
    books = Book.objects.filter(category_id=id).order_by("-created")
    return render(request, "store/category.html", {"book": Paginator(books, 10).get_page(request.GET.get("page"))})


@ensure_csrf_cookie
def get_writer(request, id):
    writer = get_object_or_404(Writer, pk=id)
    return render(request, "store/writer.html", {"wrt": writer, "book": Book.objects.filter(writer=writer)})
