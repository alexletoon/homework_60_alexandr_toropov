from django.shortcuts import render, get_object_or_404, redirect
from store_app.models import Product, Choice
from online_store.forms import ProductForm, SearchForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.utils.http import urlencode
from django.db.models import Q

# def index_view(request):
#     products = Product.objects.exclude(qty=0).exclude(is_deleted=True).order_by('name')
#     context = {'products': products, 'choice': Choice.choices}
#     return render(request, 'index.html', context=context)


class IndexView(ListView):
    template_name: str = 'index.html'
    context_object_name = 'products'
    # model = Product
    ordering = ['name']
    paginate_by = 3
    paginate_orphans: int = 1


    # def get_queryset(self):
        # return Product.objects.exclude(is_deleted=True)
    

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)
    

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


# def display_product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product, 'choices': Choice.choices}
#     return render(request, 'display_product.html', context=context)

class DisplayProductView(DetailView):
    template_name: str = 'display_product.html'
    model = Product

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['product'] = get_object_or_404(Product, pk=kwargs['pk'])
    #     return context

# def add_product_view(request):
#     product_form = ProductForm()
#     if request.method == 'GET':
#         context = {'choices': Choice.choices, 'form': product_form}
#         return render(request, 'add_product.html', context=context)
#     product_form = ProductForm(request.POST)
#     if not product_form.is_valid():
#         return render(request, 'add_product.html', context={'choices': Choice.choices, 'form': product_form})
#     product = Product.objects.create(**product_form.cleaned_data)
#     return redirect('index_view')


class AddProductView(CreateView):
    template_name: str = 'add_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/'

# def edit_product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         product_form = ProductForm(instance=product)
#         return render(request, 'edit_product.html', context={'product': product, 'form': product_form})
#     product_form = ProductForm(request.POST, instance=product)
#     if not product_form.is_valid():
#         return render (request, 'edit_product.html', context={'product': product, 'form': product_form})

#     product_form.save()
#     return redirect('index_view')


class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name: str = 'edit_product.html'
    success_url = '/'


class DeleteProductView(DeleteView):
    model = Product
    template_name: str = 'confirm_delete.html'
    success_url = '/'

# def confirm_delete_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'confirm_delete.html', context={'product': product})


# def product_deleted_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return redirect('index_view')
