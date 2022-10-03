from cProfile import label
from re import T
from django import forms
from django.forms import widgets 
from store_app.models import Product, Choice


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование")
    description = forms.CharField(max_length=2000, label='Описание', required=False, widget=widgets.Textarea)
    pic = forms.URLField(required=False, label='Фото')
    category = forms.ChoiceField(required=True, label='Категория', choices=Choice.choices, widget=widgets.Select)
    qty = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(decimal_places=2, required=True, label='Цена')