from django.views import generic
from .models import *

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'index.html'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context