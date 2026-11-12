from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("price", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "name", "email", "payable", "payment_method", "paid", "created")
    list_filter = ("paid", "payment_method", "created")
    search_fields = ("name", "email", "phone", "customer__username")
    readonly_fields = ("created", "updated", "payable", "totalbook")
    inlines = (OrderItemInline,)
