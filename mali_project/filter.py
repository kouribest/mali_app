import django_filters
from mali_project.models import BaseModel
from mali.models import MaliModel
from rdc.models import RDCModel

from django import forms

field_name= ('identifiant', 'prenom', 'nom_famille', 'type_voyage', 'allant_a', 'venant_de', 'genre')

class MaliFilter(django_filters.FilterSet):
	"""Filter queryset by providing a request.GET"""

	class Meta:
		model = MaliModel
		fields =  field_name

class RdcFilter(django_filters.FilterSet):
	"""Filter queryset by providing a request.GET"""

	class Meta:
		model = RDCModel
		fields = field_name



