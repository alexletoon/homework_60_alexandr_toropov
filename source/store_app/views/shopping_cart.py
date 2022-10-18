from itertools import product
from store_app.models import Product, ShoppingCart
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from store_app.models import Product, Order, OrderedProducts
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from online_store.forms import OrderForm


class CartView(ListView):
    template_name: str = 'shopping_cart.html'
    context_object_name = 'cart_products'
    model = ShoppingCart
    paginate_by: int = 5

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm() 
        return context


    def post(self, request, *args, **kwargs):
        order_form = OrderForm(self.request.POST)
        if order_form.is_valid():
            order=Order.objects.create(**order_form.cleaned_data)
            cart_items = ShoppingCart.objects.all()
            for item in cart_items:
                ordered_product = get_object_or_404(Product, pk=item.product.pk)
                OrderedProducts.objects.create(order=order, ordered_product=ordered_product, quantity=item.qty)
                item.delete()
        return redirect('index_view')

class CartProductDeleteView(DeleteView):
    template_name: str = 'shopping_cart.html'
    model = ShoppingCart


    def get_success_url(self) -> str:
        return reverse ('index_view')


# class MakeOrderView(CreateView):
#     template_name: str = 'shopping_cart.html'
#     form_class = OrderForm


