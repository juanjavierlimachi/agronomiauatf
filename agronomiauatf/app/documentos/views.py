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



class DocumentosListView(ListView):
    model = Documento
    template_name = "documentos/DocumentosListView.html"
    #paginate_by = 10
    #context_object_name = 'countries'


def CreateDocumento(request):
    Usuario=Documento(Usuario=request.user)
    if request.method == 'POST':
        forms=DocumentoForm(request.POST, request.FILES, instance=Usuario)
        if forms.is_valid():
            datos = forms.save(commit=False)
            datos.save()
            return HttpResponse(int(datos.id))
    else:
        forms=DocumentoForm(instance=Usuario)
    return render(request,'documentos/CreateDocumento.html',{'form':forms})

def shearDocuments(request):
    pass


class DetailDocuments(DetailView):
    model = Documento
    template_name = "documentos/DocumentoDetailView.html"


''' class UpdateDocuments(UpdateView):
    model = Documento
    success_url = reverse_lazy('documentos:detail-documents')
    template_name = "documentos/UpdateDocuments.html"
    fields=['Titulo','Categoria','Archivo'] '''


def UpdateDocuments(request, id):
    dato = Documento.objects.get(id=int(id))
    if request.method == 'POST':
        forms = DocumentoForm(request.POST, request.FILES, instance=dato)
        if forms.is_valid():
            forms.save()
            return HttpResponse('200')
    forms = DocumentoForm(instance=dato)
    return render(request, 'documentos/UpdateDocuments.html', {'form': forms, 'dato': dato})

class DeleteDocuments(DeleteView):
    model = Documento
    template_name = "documentos/DeleteDocuments.html"
    def post(self, request, *args, **kwargs):
        #print(request.POST['option'])#obtengo un dato de un input del formulario
        #print(kwargs['pk'])#diccionario de datos para obtener los datos del la url
        get_data = self.model.objects.get(pk = kwargs['pk'])
        get_data.estado = False 
        get_data.save()
        return HttpResponse('200')