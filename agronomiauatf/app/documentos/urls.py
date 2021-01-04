
from django.urls import path
from agronomiauatf.app.documentos import views
urlpatterns = [
    path('create-category', views.CreateCategory, name='category'),
    path('list-category', views.ListarCategorias.as_view(), name='list-category'),
    path('show-categoria/<int:pk>', views.ShowCategoria.as_view(), name='showCategoria'),
    path('delete-categoria/<int:pk>', views.DeleteCategoria.as_view(), name='deleteCategoria'),
]
