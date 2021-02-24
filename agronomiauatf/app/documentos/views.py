from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.views.generic import View, FormView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import User
from agronomiauatf.app.documentos.forms import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django import forms
from django.urls import reverse, reverse_lazy
from django.db.models import Q
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
    def get(self, request, *args, **kwargs):
        self.dic = {
            'object_list':self.model.objects.all().order_by('-id'),
            'categorias':Categoria.objects.all().order_by('-id')
        }
        return render(request,self.template_name, self.dic)


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
    return render(request,'documentos/shearDocuments.html',{})

def BuscarDocumento_view(request):
    if request.method=="POST":
        texto=request.POST["name_documents"]
        busqueda=(
            Q(Titulo__icontains=texto) |
            Q(Fecha_creacion__icontains=texto) |
            Q(id__icontains=texto)
        )
        resultados=Documento.objects.filter(busqueda, estado=True).distinct()
        return render(request,'documentos/searList.html',{'object_list':resultados})
    else:
        texto=request.GET["name_documents"]
        busqueda=(
            Q(Titulo__icontains=texto) |
            Q(Titulo__icontains=texto) |
            Q(id__icontains=texto)
        )
        resultados=Documento.objects.filter(busqueda, estado=True).distinct()
        return render(request,'documentos/searList.html',{'object_list':resultados}) 
class DetailDocuments(DetailView):
    model = Documento
    template_name = "documentos/DocumentoDetailView.html"
    
    def get(self, request, *args, **kwargs):
        print(kwargs)
        self.dic = {
            'coments':Comentar.objects.filter(documento_id = int(kwargs['pk'])).order_by('-id'),
            'object':Documento.objects.get(id = int(kwargs['pk']))
            #'usuarios':self.model.objects.all().count()
        }
        return render(request,self.template_name, self.dic)


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
    
def CountDoumload(request, pk):
    get_data = Documento.objects.get(id = int(pk))
    get_data.Descargas = int(get_data.Descargas) + 1
    get_data.save()
    return HttpResponse(get_data.Descargas)

def getDocumento(id_documento):
    dato = Documento.objects.get(id = int(id_documento))
    return dato

from smtplib import SMTP
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from datetime import datetime, date, time, timedelta

def sharedFile(request, pk):
    
    Usuario=Compartir(Usuario=request.user)
    if request.method == 'POST':
        forms=CompartirForm(request.POST,instance=Usuario)
        if forms.is_valid():
            datos = forms.save(commit=False)
            datos.Correo_origen = settings.EMAIL_HOST_USER
            datos.Correo_Destino = request.POST['Correo_Destino']
            datos.documento_id = int(pk)
            
            body = render_to_string('documentos/dato_compartido.html',{
                'documento':getDocumento(pk),
                'date_today':datetime.now(),
                'usuario':User.objects.get(id=int(request.user.id))
                },
            )
            #a  = request.FILES["Archivo"]
            email_message = EmailMessage(
                subject = f'Documento Compartido {pk}',
                body = body,
                from_email = settings.EMAIL_HOST_USER,
                to = [request.POST['Correo_Destino']]
            )
            #email.attach(a.name, a.read(), a.content_type)
            #a.close()
            email_message.content_subtype = 'html'
            email_message.send()
            datos.save()

            return HttpResponse("200")
    else:
        forms=CompartirForm(instance=Usuario)
    return render(request,'documentos/sharedFile.html',{'form':forms,'pk':pk})

def CreateComents(request, id_document):
    Usuario=Comentar(Usuario=request.user)
    if request.method == 'POST':
        forms=ComentForm(request.POST,instance=Usuario)
        if forms.is_valid():
            datos = forms.save(commit=False)
            datos.documento_id = int(id_document)
            
            datos.save()
            return HttpResponse("200")
    else:
        forms=ComentForm(instance=Usuario)
    return render(request,'documentos/CreateComents.html',{'form':forms,'id_document':id_document})


class ListCompartidos(ListView):
        model = Compartir
        template_name = "documentos/ListCompartidos.html"
        ''' 
            method to attach data in context
            def get_context_data(self, **kwargs): 
            context = super(ListCompartidos, self).get_context_data(**kwargs)
            context['object_list'] = self.model.objects.filter(estado=True)
            print(kwargs)
            return context '''
        
        def get(self, request, *args, **kwargs):
            self.dic = {
                'object_list':self.model.objects.filter(documento_id = int(kwargs['id_document'])).order_by('-id')
                #'usuarios':self.model.objects.all().count()
            }
            return render(request,self.template_name, self.dic)
        
class ListComentarios(ListView):
    model = Comentar
    template_name = "documentos/ListComentarios.html"
    def get(self, request, *args, **kwargs):
        self.dic = {
            'object_list':self.model.objects.filter(documento_id = int(kwargs['id_document'])).order_by('-id')
        }
        return render(request,self.template_name, self.dic)



class ComentarDeleteView(DeleteView):
    model = Comentar
    template_name = "documentos/ComentarDeleteView.html"
    def post(self, request, *args, **kwargs):
        #print(request.POST['option'])#obtengo un dato de un input del formulario
        #print(kwargs['pk'])#diccionario de datos para obtener los datos del la url
        get_data = self.model.objects.get(pk = kwargs['pk'])
        get_data.estado = False 
        get_data.save()
        return HttpResponse('200')
    
def editComent(request, id_coment, id_document):
    dato = Comentar.objects.get(id=int(id_coment))
    if request.method == 'POST':
        forms = ComentForm(request.POST, instance=dato)
        if forms.is_valid():
            forms.save()
            return HttpResponse('200')
    forms = ComentForm(instance=dato)
    return render(request, 'documentos/editComent.html', {'form': forms,'dato':dato})


def selectDocument(request, id_categoria):
    documento = Documento.objects.filter(Categoria_id=int(id_categoria))
    return render(request,'documentos/selectDocument.html',{'documentos':documento})

def printDcocumentos(request, id_categoria):
    documento = Documento.objects.filter(Categoria_id=int(id_categoria))
    return render(request,'documentos/printDcocumentos.html',{'documentos':documento})

def rangoFechas(request):
    if request.method == 'POST':
        pass
    dic = {
        'users':User.objects.filter(is_superuser = True, is_staff = True)
    }
    return render(request,'documentos/rangoFechas.html',dic)

def reportGeneral(request, clients_id, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio,"%d-%m-%Y")
    fecha_fin = datetime.strptime(fecha_fin,"%d-%m-%Y")
    #fecha_fin = fecha_fin + timedelta(days=1)
    if str(fecha_inicio) > str(fecha_fin):
        return HttpResponse("Error: La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
    if int(clients_id) == 0:# if you don't choose any customer
        user = 0
        documentos = Documento.objects.filter(Fecha_creacion__range=(fecha_inicio,fecha_fin),estado = True).order_by('Fecha_creacion')
    else:
        user = User.objects.get(id=int(clients_id))
        documentos = Documento.objects.filter(Fecha_creacion__range=(fecha_inicio,fecha_fin),estado = True, Usuario_id=int(clients_id)).order_by('Fecha_creacion')
    dic={
        'user':user,
        'documentos':documentos
    }
    print(dic)
    return render(request, 'documentos/selectDocument.html',dic)

def printReportGeneral(request, clients_id, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio,"%d-%m-%Y")
    fecha_fin = datetime.strptime(fecha_fin,"%d-%m-%Y")
    #fecha_fin = fecha_fin + timedelta(days=1)
    if str(fecha_inicio) > str(fecha_fin):
        return HttpResponse("Error: La Fecha Inicio No pueder ser Mayor a la Fecha Final.")
    if int(clients_id) == 0:# if you don't choose any customer
        user = 0
        documentos = Documento.objects.filter(Fecha_creacion__range=(fecha_inicio,fecha_fin),estado = True).order_by('Fecha_creacion')
    else:
        user = User.objects.get(id=int(clients_id))
        documentos = Documento.objects.filter(Fecha_creacion__range=(fecha_inicio,fecha_fin),estado = True, Usuario_id=int(clients_id)).order_by('Fecha_creacion')
    dic={
        'user':user,
        'documentos':documentos
    }
    print(dic)
    return render(request, 'documentos/printReportGeneral.html',dic)
