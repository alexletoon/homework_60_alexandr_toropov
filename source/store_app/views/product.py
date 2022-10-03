from django.shortcuts import render, get_object_or_404, redirect
from store_app.models import Product, Choice
from online_store.forms import ProductForm

def index_view(request):
    products = Product.objects.exclude(qty=0).order_by('name')
    context = {'products': products, 'choices': Choice.choices}
    return render(request, 'index.html', context=context)


def display_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product, 'choice': Choice.choices}
    return render(request, 'display_product.html', context=context)


def add_product_view(request):
    product_form = ProductForm()
    if request.method == 'GET':
        context = {'choices': Choice.choices, 'form': product_form}
        return render(request, 'add_product.html', context=context)
    product_form = ProductForm(request.POST)
    if not product_form.is_valid():
        return render(request, 'add_product.html', context={'choices': Choice.choices, 'form': product_form})
    product = Product.objects.create(**product_form.cleaned_data)
    return redirect('index_view')
