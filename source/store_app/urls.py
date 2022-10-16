
from django.urls import path
from store_app.views.product import IndexView, DisplayProductView, AddProductView, EditProductView, confirm_delete_view, product_deleted_view


urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path('product/<int:pk>', DisplayProductView.as_view(), name='display_product'),
    path('product/create', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('product/confirm_delete/<int:pk>', confirm_delete_view, name='confirm_delete'),
    path('product/product_deleted/<int:pk>', product_deleted_view, name='product_deleted')
]