from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserResource(resources.ModelResource):
	class Meta:
		model = User
		fields = ('id','username','first_name', 'email', 'is_superuser','last_login')
class UserAdmin(ImportExportModelAdmin):
	resource_class = UserResource
#admin.site.register(Categoria)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)