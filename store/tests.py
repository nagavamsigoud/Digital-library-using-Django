from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Writer, Book, Review

class BookReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reader", password="Strong-pass-123")
        category = Category.objects.create(name="Fiction", slug="fiction")
        writer = Writer.objects.create(name="Writer", slug="writer", bio="Bio")
        self.book = Book.objects.create(writer=writer, category=category, name="Test book", slug="test-book", price=100, stock=5, description="Test")

    def test_review_requires_login(self):
        response = self.client.post(reverse("store:book", args=[self.book.pk]), {"review_star": 5, "review_text": "Good"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 0)

    def test_authenticated_user_can_submit_review(self):
        self.client.login(username="reader", password="Strong-pass-123")
        response = self.client.post(reverse("store:book", args=[self.book.pk]), {"review_star": 5, "review_text": "Good"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.get().customer, self.user)

    def test_review_rating_must_be_one_to_five(self):
        self.client.login(username="reader", password="Strong-pass-123")
        self.client.post(reverse("store:book", args=[self.book.pk]), {"review_star": 8, "review_text": "Bad rating"})
        self.assertEqual(Review.objects.count(), 0)
