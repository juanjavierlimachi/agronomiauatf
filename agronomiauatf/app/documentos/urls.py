
from django.urls import path
from agronomiauatf.app.documentos import views
urlpatterns = [
    path('create-category', views.CreateCategory, name='category'),
    path('list-category', views.ListarCategorias.as_view(), name='list-category'),
    path('show-categoria/<int:pk>', views.ShowCategoria.as_view(), name='showCategoria'),
    path('delete-categoria/<int:pk>', views.DeleteCategoria.as_view(), name='deleteCategoria'),
    
    path('list-documents/', views.DocumentosListView.as_view(), name='list-documents'),
    path('create-documents/', views.CreateDocumento, name='documents'),
    path('shearDocuments/', views.shearDocuments, name='shearDocuments'),
    path('detail-documents/<int:pk>', views.DetailDocuments.as_view(), name='detail-documents'),
    path('update-documents/<int:id>', views.UpdateDocuments, name='update-documents'),
    path('delete-documents/<int:pk>', views.DeleteDocuments.as_view(), name='deleteDocuments'),
]
