
from django.urls import path
from store_app.views.product import IndexView, DisplayProductView, AddProductView, EditProductView, DeleteProductView


urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path('product/<int:pk>', DisplayProductView.as_view(), name='display_product'),
    path('product/create', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('product/confirm_delete/<int:pk>', DeleteProductView.as_view(), name='confirm_delete'),
]