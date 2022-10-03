from django.urls import path
from store_app.views.product import index_view, display_product_view, add_product_view, edit_product_view, confirm_delete_view, product_deleted_view


urlpatterns = [
    path("", index_view, name='index_view'),
    path('product/<int:pk>', display_product_view, name='display_product'),
    path('product/create', add_product_view, name='add_product'),
    path('product/edit/<int:pk>', edit_product_view, name='edit_product'),
    path('product/confirm_delete/<int:pk>', confirm_delete_view, name='confirm_delete'),
    path('product/product_deleted/<int:pk>', product_deleted_view, name='product_deleted')
]