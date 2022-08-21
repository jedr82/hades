from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
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

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una categoría'
        context['list_url'] = reverse_lazy('erp_app:category_list')
        context['entity'] = 'Categorías'
        context['action'] = 'add'
        return context

class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp_app:category_list')

    def dispatch(self,request,*args,**kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una categoría'
        context['list_url'] = reverse_lazy('erp_app:category_list')
        context['entity'] = 'Categorías'
        context['action'] = 'edit'
        return context

class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp_app:category_list')

    def dispatch(self,request,*args,**kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una categoría'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp_app:category_list')
        return context