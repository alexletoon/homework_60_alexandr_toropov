from django.shortcuts import render
from store_app.models import Product

def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context=context)