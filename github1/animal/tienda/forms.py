from django import forms
from .models import Producto
from .models import Persona


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields ='__all__'


class PersonaForm(forms.ModelForm):
    class Meta:
        model= Persona
        fields ='__all__'