from django.forms import *
from .models import Category, Client, Product
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