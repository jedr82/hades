from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import *
from .forms import CategoryForm, ClientForm, ProductForm, SaleForm, TestForm, TestForm2

# Dashboard
class Dashboard(generic.TemplateView):
    template_name = 'layout/collapsed_sidebar/index.html'

#TestView
class TestView(generic.TemplateView):
    template_name = 'test.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = []
                for i in Product.objects.filter(cate_id=request.POST['id']):
                    data.append({'id': i.id, 'name': i.name})

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados | Django'
        context['form'] = TestForm()
        return context

#TestView2
class TestView2(generic.TemplateView):
    template_name = 'test2.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id':'','text':'------'}]
                for i in Product.objects.filter(cate_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name})
            elif action == 'autocomplete':
                data = []
                for i in Category.objects.filter(name__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            elif action == 'autocomplete2':
                data = []
                for i in Category.objects.filter(name__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados con Select2| Django'
        context['form'] = TestForm2()
        return context
    

#Category
class CategoryListView(LoginRequiredMixin,generic.ListView):
    model = Category
    template_name = 'category/list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*arg,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error al cargar la tabla'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp_app:category_new')
        context['list_url'] = reverse_lazy('erp_app:category_list')
        context['entity'] = 'Categorías'
        return context

class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
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

class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
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

class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):

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

#Products
class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'product/list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*arg,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error al cargar la tabla'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('erp_app:product_new')
        context['list_url'] = reverse_lazy('erp_app:product_list')
        context['entity'] = 'Productos'
        return context

class ProductoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('erp_app:product_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            print(request.POST)
            print(request.FILES)
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
        context['title'] = 'Creación de un producto'
        context['list_url'] = reverse_lazy('erp_app:product_list')
        context['entity'] = 'Productos'
        context['action'] = 'add'
        return context

class ProductoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('erp_app:product_list')

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
        context['title'] = 'Edición de un producto'
        context['list_url'] = reverse_lazy('erp_app:product_list')
        context['entity'] = 'Producto'
        context['action'] = 'edit'
        return context

class ProductoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('erp_app:product_list')

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
        context['title'] = 'Eliminación de un producto'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('erp_app:product_list')
        return context

#Clients
class ClientView(LoginRequiredMixin, generic.TemplateView):
    model = Client
    template_name = 'client/list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchData':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            elif action == "add":
                cli = Client()
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.dni = request.POST['dni']
                cli.date_birthday = request.POST['date_birthday']
                cli.address = request.POST['address']
                cli.gender = request.POST['gender']
                cli.save()
            elif action == "edit":
                cli = Client.objects.get(pk=request.POST['id'])
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.dni = request.POST['dni']
                cli.date_birthday = request.POST['date_birthday']
                cli.address = request.POST['address']
                cli.gender = request.POST['gender']
                cli.save()
            elif action == 'delete':
                cli = Client.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nuevo cliente'
        context['form'] = ClientForm()
        context['list_url'] = reverse_lazy('erp_app:client')
        context['entity'] = 'Clientes'
        return context

class SaleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy('erp_app:dashboard')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(name__icontains=request.POST['term'])
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            else:
                data['error'] = 'No se ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Venta'
        context['entity'] = 'Ventas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context