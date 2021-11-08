from django.contrib import admin
from shop.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'updated', 'price', 'available', 'created',)
    list_filter = ('name', 'category', 'price', 'available',)
    list_editable = ['price', 'available',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)