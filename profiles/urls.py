from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('order-history/<str:order_number>/', views.order_history, name='order_history'),
]
