from store_app.models import Product, ShoppingCart
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from store_app.models import Product
from django.shortcuts import render, get_object_or_404, redirect


class AddToCartView(CreateView):
    template_name: str = 'add_to_cart.html'
    model = ShoppingCart
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])
        return context

