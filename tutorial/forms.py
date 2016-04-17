from .models import Alumnos
from django.forms import ModelForm
from django import forms

class AlumnosFORM(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('nombre','apellido','domicilio','telefono')
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

