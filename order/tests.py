from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Category, Writer, Book
from .models import Order

class OrderPrivacyTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="Strong-pass-123")
        self.other = User.objects.create_user(username="other", password="Strong-pass-123")
        self.order = Order.objects.create(customer=self.owner, name="Owner", email="owner@example.com", phone="123456", address="Address", division="Bacolod City", district="Brgy.1", zip_code="6100", payment_method="Cash on delivery", payable=100, totalbook=1)

    def test_order_list_requires_login(self):
        response = self.client.get(reverse("order:order_list"))
        self.assertEqual(response.status_code, 302)

    def test_user_cannot_view_another_users_order(self):
        self.client.login(username="other", password="Strong-pass-123")
        response = self.client.get(reverse("order:order_details", args=[self.order.pk]))
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_download_another_users_invoice(self):
        self.client.login(username="other", password="Strong-pass-123")
        response = self.client.get(reverse("order:pdf", args=[self.order.pk]))
        self.assertEqual(response.status_code, 404)
