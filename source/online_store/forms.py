from cProfile import label
from re import T
from django import forms
from django.forms import widgets 
from store_app.models import Product, Choice


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','category', 'pic', 'qty', 'price']