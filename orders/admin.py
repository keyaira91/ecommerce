from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity', 'product', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email','postal_code', 'city', 'postal_code', 'paid']
    list_filter = ['postal_code', 'city', 'created', 'paid']
    inlines = [OrderItemInline,]