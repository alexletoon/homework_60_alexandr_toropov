from django.contrib import admin
from store_app.models import Product, ShoppingCart


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'qty', 'price', 'created_at', 'is_deleted']
    list_filter = ['id', 'name', 'category', 'qty', 'price', 'created_at']
    search_fields=['id', 'name', 'category', 'price', 'created_at']
    fields= ['name', 'category', 'qty', 'price', 'pic', 'is_deleted']
    readonly_fields=['created_at', 'changed_at']


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'qty']
    list_filter = ['id', 'product', 'qty']
    search_fields = ['id', 'product', 'qty']
    fields = ['product', 'qty']

admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
