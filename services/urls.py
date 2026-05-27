from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]
