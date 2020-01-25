from django.contrib import admin
from mali.models import MaliModel as mali
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class MaliAdmin(ImportExportActionModelAdmin):
	list_display=  [f.name for f in mali._meta.fields]
	list_filter= ['genre', 'type_voyage', 'date_enregistrement']
	search_fields= ('nom_famille', 'prenom', 'numero_passport')


		
admin.site.register(mali, MaliAdmin)
# Register your models here.
