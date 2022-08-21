from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import CategoryForm

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'index.html'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp_app:category_new')
        context['list_url'] = reverse_lazy('erp_app:category_list')
        context['entity'] = 'Categorías'
        return context

class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp_app:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un categoría'
        context['list_url'] = reverse_lazy('erp_app:category_list')
        context['entity'] = 'Categorías'
        return context