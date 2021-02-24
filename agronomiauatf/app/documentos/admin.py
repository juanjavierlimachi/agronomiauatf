from django.contrib import admin
from agronomiauatf.app.documentos.models import *
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Documento)
admin.site.register(Comentar)
admin.site.register(Compartir)