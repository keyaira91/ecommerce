from django.contrib import admin
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.detail_view, name='product_detail'),

]