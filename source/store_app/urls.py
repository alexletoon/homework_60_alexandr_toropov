from django.urls import path
from store_app.views.product import index_view, display_product_view


urlpatterns = [
    path("", index_view, name='index_view'),
    path('/product/<int:pk>', display_product_view, name='display_product')
]