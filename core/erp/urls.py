from django.urls import path
from .views import *

app_name = 'erp_app'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),

    #Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_new'),
]
