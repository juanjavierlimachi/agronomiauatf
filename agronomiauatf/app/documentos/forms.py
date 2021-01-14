#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from .forms import *
from django.contrib.auth.forms import User

class CategoriaForm(forms.ModelForm):
    """Form definition for Categoria."""
    #estado = forms.BooleanField(required=True, label="Actualmente activo", help_text="Decea eliminar la categoria?. has click aquí")
    class Meta:
        """Meta definition for Categoriaform."""

        model = Categoria
        #fields = ('Nombre_categoria','estado',)
        exclude=('estado',)

class DocumentoForm(forms.ModelForm):
    """Form definition for DocumentoForm."""

    class Meta:
        """Meta definition for DocumentoForm."""

        model = Documento
        #fields = ('Titulo',)
        exclude=('Usuario','estado',)
