from django.urls import path
from .views import *

app_name = 'erp_app'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

    #Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', CategoryListView2.as_view(), name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_new'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
