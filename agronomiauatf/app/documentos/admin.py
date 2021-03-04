from django.contrib import admin
from agronomiauatf.app.documentos.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DocumentoResource(resources.ModelResource):
	class Meta:
		model = Documento
class DocumentoAdmin(ImportExportModelAdmin):
	resource_class = DocumentoResource

admin.site.register(Categoria)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Comentar)
admin.site.register(Compartir)

