from django.contrib import admin
from rdc.models import RDCModel as congo
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class RDCAdmin(ImportExportActionModelAdmin):
	list_display=  [f.name for f in congo._meta.fields]
	list_filter= ['genre', 'type_voyage', 'date_enregistrement']
	search_fields= ('nom_famille', 'prenom', 'numero_passport')


admin.site.register(congo, RDCAdmin)

# Register your models here.
