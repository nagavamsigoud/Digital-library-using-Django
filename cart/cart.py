"""Session-backed shopping cart."""
from decimal import Decimal
from django.conf import settings
from store.models import Book

MAX_ITEM_QUANTITY = 10

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault(settings.CART_SESSION_ID, {})

    def add(self, book, quantity=1):
        book_id = str(book.pk)
        current = self.cart.get(book_id, {}).get("quantity", 0)
        new_quantity = min(MAX_ITEM_QUANTITY, current + int(quantity))
        if new_quantity < 1:
            raise ValueError("Quantity must be at least one.")
        if new_quantity > book.stock:
            new_quantity = book.stock
        if new_quantity < 1:
            raise ValueError("This book is currently out of stock.")
        self.cart[book_id] = {"quantity": new_quantity, "price": str(book.price)}
        self.save()

    def update(self, book, quantity):
        quantity = int(quantity)
        if quantity < 1 or quantity > MAX_ITEM_QUANTITY:
            raise ValueError(f"Quantity must be between 1 and {MAX_ITEM_QUANTITY}.")
        if quantity > book.stock:
            raise ValueError("Requested quantity exceeds available stock.")
        book_id = str(book.pk)
        if book_id not in self.cart:
            raise KeyError("Book is not in the cart.")
        self.cart[book_id]["quantity"] = quantity
        self.cart[book_id]["price"] = str(book.price)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, book):
        self.cart.pop(str(book.pk), None)
        self.save()

    
    def __iter__(self):
        ids = list(self.cart.keys())
        books = Book.objects.filter(pk__in=ids)

        valid_ids = {str(book.pk) for book in books}

        for stale_id in set(ids) - valid_ids:
            self.cart.pop(stale_id, None)

        for book in books:
            item = self.cart[str(book.pk)].copy()
            item["book"] = book
            item["price"] = Decimal(str(book.price))
            item["total_price"] = item["price"] * int(item["quantity"])
            yield item

        self.save()

    def __len__(self):
        return sum(
            int(item.get("quantity", 0))
            for item in self.cart.values()
        )

    def get_total_price(self):
        total = Decimal("0.00")

        for book_id in list(self.cart.keys()):
            try:
                book = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                self.cart.pop(book_id, None)
                continue

            quantity = int(self.cart[book_id]["quantity"])
            self.cart[book_id]["price"] = str(book.price)

            total += Decimal(str(book.price)) * quantity

        self.save()
        return total

    def clear(self):
        self.cart = {}
        self.session.pop(settings.CART_SESSION_ID, None)
        self.session.modified = True
