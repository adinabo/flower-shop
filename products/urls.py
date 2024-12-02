from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('bag/add/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('add/', views.add_product, name='add_product'),
]