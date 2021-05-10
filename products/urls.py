from django.urls import path
from .views import view_all_products, add_product_view, product_details, ProductView, list_view

app_name = 'products'

urlpatterns = [
    path('view_all_products/', list_view, name='view_all_products'),
    path('add_product/', add_product_view, name='add_product'),
    path('<int:product_id>/', product_details, name='details'),
    # path('<int:product_id>/add_to_cart/', add_to_cart, name='add_to_cart'),
]
