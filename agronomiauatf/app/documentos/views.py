from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.views.generic import View, FormView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import User
from agronomiauatf.app.documentos.forms import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django import forms
from django.urls import reverse, reverse_lazy
#from django.core.urlresolvers import reverse_lazy
# Create your views here.

class ListarCategorias(ListView):
    model = Categoria
    template_name = "documentos/CategoriaListView.html"


def CreateCategory(request):
    if request.method == 'POST':
        forms=CategoriaForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse("200")
    else:
        forms=CategoriaForm()
    return render(request,'documentos/CreateCategory.html',{'form':forms})

class ShowCategoria(UpdateView):
    model = Categoria
    template_name = "documentos/ShowCategoria.html"
    fields = ['Nombre_categoria']
    #@method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        #print(request.POST['option'])#obtengo un dato de un input del formulario
        #print(kwargs['pk'])#diccionario de datos para obtener los datos del la url
        get_categoria = self.model.objects.get(pk = kwargs['pk'])
        print(get_categoria)
        get_categoria.Nombre_categoria = request.POST['Nombre_categoria']
        get_categoria.save()
        return HttpResponse('La categoria actualizo correctamente')


class DeleteCategoria(DeleteView):
    model = Categoria
    template_name = "documentos/CategoriaDeleteView.html"
    def post(self, request, *args, **kwargs):
        #print(request.POST['option'])#obtengo un dato de un input del formulario
        #print(kwargs['pk'])#diccionario de datos para obtener los datos del la url
        get_categoria = self.model.objects.get(pk = kwargs['pk'])
        get_categoria.estado = False 
        get_categoria.save()
        return HttpResponse('200')