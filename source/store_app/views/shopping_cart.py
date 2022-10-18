from itertools import product
from store_app.models import Product, ShoppingCart
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from store_app.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


class CartView(ListView):
    template_name: str = 'shopping_cart.html'
    context_object_name = 'cart_products'
    model = ShoppingCart
    paginate_by: int = 5

    
class CartProductDeleteView(DeleteView):
    template_name: str = 'shopping_cart.html'
    model = ShoppingCart


    def get_success_url(self) -> str:
        return reverse ('index_view')

