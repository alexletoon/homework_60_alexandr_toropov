from django.shortcuts import render, get_object_or_404, redirect
from store_app.models import Product, Choice, ShoppingCart
from online_store.forms import ProductForm, SearchForm, CartForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.utils.http import urlencode
from django.db.models import Q


class IndexView(ListView):
    template_name: str = 'index.html'
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 3
    paginate_orphans: int = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('pk')
        # product_count = 0
        product_count = 1
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if ShoppingCart.objects.filter(product=product).exists():
            existing_cart_item = ShoppingCart.objects.get(product_id=product_id)
            existing_cart_item.qty+=1
            existing_cart_item.save()
        else:
            ShoppingCart.objects.create(product_id=product_id, qty=product_count)
        return redirect('index_view')
            


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

        
    def get_queryset(self):
        queryset = Product.objects.exclude(is_deleted=True)
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset


    def get_search_form(self):
        return SearchForm(self.request.GET)
    
        
    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class DisplayProductView(DetailView):
    template_name: str = 'display_product.html'
    model = Product

    # def post(self, request, *args, **kwargs):

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['add_to_cart'] = CartForm




class AddProductView(CreateView):
    template_name: str = 'add_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/'

class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name: str = 'edit_product.html'
    success_url = '/'


class DeleteProductView(DeleteView):
    model = Product
    template_name: str = 'confirm_delete.html'
    success_url = '/'

