from django.shortcuts import render, get_object_or_404
from store_app.models import Product, Choice

def index_view(request):
    products = Product.objects.exclude(qty=0).order_by('name')
    context = {'products': products, 'choices': Choice.choices}
    return render(request, 'index.html', context=context)


def display_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product, 'choice': Choice.choices}
    return render(request, 'display_product.html', context=context)