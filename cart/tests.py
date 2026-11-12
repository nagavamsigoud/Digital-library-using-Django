from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from store.models import Category, Writer, Book
from .cart import Cart

class CartTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Fiction", slug="fiction")
        writer = Writer.objects.create(name="Writer", slug="writer", bio="Bio")
        self.book = Book.objects.create(writer=writer, category=category, name="Test book", slug="test-book", price=100, stock=5, description="Test")
        self.request = RequestFactory().get("/")
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(self.request)
        self.request.session.save()

    def test_add_and_total(self):
        cart = Cart(self.request)
        cart.add(self.book)
        self.assertEqual(len(cart), 1)
        self.assertEqual(str(cart.get_total_price()), "100.00")

    def test_update_rejects_invalid_quantity(self):
        cart = Cart(self.request)
        cart.add(self.book)
        with self.assertRaises(ValueError):
            cart.update(self.book, 0)

    def test_clear(self):
        cart = Cart(self.request)
        cart.add(self.book)
        cart.clear()
        self.assertEqual(len(cart), 0)
