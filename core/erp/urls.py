from django.urls import path
from .views import *

app_name = 'erp_app'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

    #Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_new'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    #Producto
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductoCreateView.as_view(), name='product_new'),
    path('product/edit/<int:pk>/', ProductoUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductoDeleteView.as_view(), name='product_delete'),
]
