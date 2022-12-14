from django.forms import *
from .models import Category, Client, Product, Sale
from datetime import datetime

class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre'
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder':'Detalle de la descripción',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProductForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class':'form-control',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=Category.objects.none(), widget=Select(attrs={
        'class':'form-control',
        'style': 'width: 100%'
    }))

class TestForm2(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class':'form-control select2',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=Category.objects.none(), widget=Select(attrs={
        'class':'form-control select2',
        'style': 'width: 100%'
    }))

    search = CharField(widget=TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ingrese una descripción'
    }))

    search2 = ModelChoiceField(queryset=Category.objects.none(), widget=Select(attrs={
        'class':'form-control select2',
        'style': 'width: 100%'
    }))

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder':'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder':'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder':'Ingrese su Dni',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',attrs={
                'value': datetime.now().strftime('%Y-%m-%d'),
            }),
            'address': TextInput(
                attrs={
                    'placeholder':'Ingrese su dirección'
                }
            ),
            'gender': Select()
        }
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str(e)
        return data

class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

        #Forma1
        self.fields['cli'].widget.attrs['autofocus'] = True
        self.fields['cli'].widget.attrs['class'] = 'form-control select2'
        self.fields['cli'].widget.attrs['style'] = 'width: 100%'

        #Forma2
        self.fields['date_joined'].widget.attrs ={
            'autocomplete':'off',
            'class':'form-control datetimepicker-input',
            'id':'date_joined',
            'data_target':'#date_joined',
            'data-toggle':'datetimepicker'
        }

        self.fields['subtotal'].widget.attrs = {
            'class':'form-control',
            'disabled':True
        }

        self.fields['total'].widget.attrs = {
            'class':'form-control',
            'disabled':True
        }

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class':'form-control select2',
                'style':'width: 100%'
            }),

            'date_joined': DateInput(format='%Y-%m-%d', attrs={
                'value':datetime.now().strftime('%Y-%m-%d')
            }),

            'iva': TextInput()
        }