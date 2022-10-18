
from django.urls import path
from store_app.views.product import IndexView, DisplayProductView, AddProductView, EditProductView, DeleteProductView
from store_app.views.shopping_cart import CartView, CartProductDeleteView


urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path('product/<int:pk>', DisplayProductView.as_view(), name='display_product'),
    path('product/create', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('product/confirm_delete/<int:pk>', DeleteProductView.as_view(), name='confirm_delete'),
    path('product/<int:pk>/add_to_cart/', IndexView.as_view(), name='add_to_cart'),
    path('shopping_cart/', CartView.as_view(), name='shopping_cart'),
    path('shopping_cart/delete_product/<int:pk>', CartProductDeleteView.as_view(), name='delete_cart_product'),
]