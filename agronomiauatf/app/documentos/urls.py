#encoding:utf-8
from django.urls import path
from django.conf.urls import url
from agronomiauatf.app.documentos import views
urlpatterns = [
    path('create-category', views.CreateCategory, name='category'),
    path('list-category', views.ListarCategorias.as_view(), name='list-category'),
    path('show-categoria/<int:pk>', views.ShowCategoria.as_view(), name='showCategoria'),
    path('delete-categoria/<int:pk>', views.DeleteCategoria.as_view(), name='deleteCategoria'),
    
    path('list-documents/', views.DocumentosListView.as_view(), name='list-documents'),
    path('create-documents/', views.CreateDocumento, name='documents'),
    path('shearDocuments/', views.shearDocuments, name='shearDocuments'),
    path('BuscarDocumento_view/', views.BuscarDocumento_view, name='BuscarDocumento_view'),
    path('detail-documents/<int:pk>', views.DetailDocuments.as_view(), name='detail-documents'),
    path('update-documents/<int:id>', views.UpdateDocuments, name='update-documents'),
    path('delete-documents/<int:pk>', views.DeleteDocuments.as_view(), name='deleteDocuments'),
    
    path('countDoumload/<int:pk>', views.CountDoumload, name='count-dounload'),
    path('sharedFile/<int:pk>', views.sharedFile, name='sharedFiles'),
    path('list-compartidos/<int:id_document>', views.ListCompartidos.as_view(), name='listCompartidos'),
    path('comentsFile/<int:id_document>', views.CreateComents, name='new-coments'),
    path('list-comentarios/<int:id_document>', views.ListComentarios.as_view(), name='list-comentarios'),
    path('delete-coment/<int:pk>/<int:id_document>', views.ComentarDeleteView.as_view(), name='delete-coment'),
    path('edit-coment/<int:id_coment>/<int:id_document>', views.editComent, name='edit-coment'),
    #path('edit-shear/<int:pk>/<int:id_document>', views.CompartirUpdateView.as_view(), name=''),
    path('select_documents/<int:id_categoria>', views.selectDocument, name='select_documents'),
    path('print_doc_categorias/<int:id_categoria>', views.printDcocumentos, name='print_doc_categorias'),
    
    path('rango_fechas/', views.rangoFechas, name='rango_fechas'),
    
    url(r'^report-general/(?P<clients_id>\d+)/(?P<fecha_inicio>[^/]+)/(?P<fecha_fin>[^/]+)/$',views.reportGeneral),
    url(r'^print-report-general/(?P<clients_id>\d+)/(?P<fecha_inicio>[^/]+)/(?P<fecha_fin>[^/]+)/$',views.printReportGeneral),
    #bakup de la DB
    path('generate_bakup/', views.generateBakup, name='generate_bakup'),
    
    path('createBackup/', views.createBackup, name='createBackup'),
]
