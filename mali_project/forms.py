# -*- coding: utf-8 -*
from django import forms
from django.urls import reverse
from mali_project.models import BaseModel, Message
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from mali_project.settings import STATIC_ROOT
import os, qrcode
from datetime import datetime, timedelta

ICON_GENRE = (
	(u"Homme", u"Homme|man"),
	(u"Femme", u"Femme|woman"),
)

RADIO_CHOICES=(
	(u"Oui",u"Oui"),
	(u"Non",u"Non")
)

TYPE_VOYAGE=(
	('Vol','Vol|plane'),
	('Navire', 'Navire|anchor'),
	('Voiture', 'Voiture|car'),
	('Autre', 'Autre')
)

TYPE_VOYAGE_DEFAULT=(
	('', ''),
	('Vol','Vol|plane'),
	('Navire', 'Navire|anchor'),
	('Voiture', 'Voiture|car'),
	('Autre', 'Autre')
)
STATE=(
	(u"Invalide",u"Non valide"),
	(u"Valide",u"Valide"),	
)

class FormBase(forms.ModelForm):
	genre = forms.ChoiceField(choices= ICON_GENRE, widget=forms.TextInput(attrs={"_override": "IconSelect"}))
	type_voyage = forms.ChoiceField(label= 'Moyen de voyage', choices= TYPE_VOYAGE, initial='Vol', widget=forms.TextInput(attrs={"_override":"IconSelect", "id":"id_type_voyage"}))


	def save(self, commit=True):

		qrcode_data = self.cleaned_data['identifiant']
		path = os.path.join(STATIC_ROOT, 'img', str(qrcode_data)+'.jpeg')

		# Generer un nouveau QRCode si le formulaire n'en pas deja 
		if not os.path.exists(path): 
			qr = qrcode.QRCode(
				version=2,
				error_correction=qrcode.constants.ERROR_CORRECT_H,
				box_size=30,
				border=4,
			)
			qr.add_data(qrcode_data)
			qr.make(fit=True)
			img = qr.make_image()
			try:
				img.save(path)
			except Exception as e:
				raise e #handle IOError here
	
		return super(FormBase, self).save(commit=True)

	def clean_date_enregistrement(self):
		pass

	def clean_date_voyage(self):
		data = self.cleaned_data['date_voyage']
		date_voyage = data.date()
		today_date= datetime.utcnow().date()
		if date_voyage < today_date:
			raise forms.ValidationError(('Vous ne pouvez enregistrer un voyage anterieur'))
		return date_voyage

	class Meta:
		fields = '__all__'
		model = BaseModel
		widgets = {
			'domain': forms.HiddenInput(attrs=({'readonly': 'readonly'})),
			'etat': forms.HiddenInput(attrs={'readonly': 'readonly'}),
			'identifiant': forms.TextInput(attrs=({'readonly': 'readonly'})),
			'genre': forms.TextInput(attrs={'_icon': 'genderless'}),
			'numero_matricule': forms.TextInput(attrs={'class':'Voiture_input'}),
			'nom_compagnie': forms.TextInput(attrs={'class':'Voiture_input'}),
			'nom_bateau': forms.TextInput(attrs={'class':'Navire_input'}),
			'numero_cabine': forms.TextInput(attrs={'class':'Navire_input'}),
			'numero_siege': forms.TextInput(attrs={'class':'Vol_input'}),
			'numero_vol': forms.TextInput(attrs={'class':'Vol_input'})
		} 

class FilterForm(FormBase):
	type_voyage = forms.ChoiceField(choices= TYPE_VOYAGE_DEFAULT, initial='', widget=forms.TextInput(attrs={"_override":"IconSelect", "id":"id_type_voyage"}))
	def __init__(self, *args, **kwargs):
		super(FilterForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			self.fields[field_name].required = False

	class Meta(FormBase.Meta):
		fields = ('date_voyage', 'type_voyage', 'allant_a', 'venant_de', 'genre')
		layout=[
			("two Fields",
				("Field", "date_voyage"),
				("Field", "type_voyage"),
			),
			("Text", "<div class='ui divider'></div>"),
			("Field", "genre"),
			("Text", "<div class='ui divider'></div>"),
			("two Fields",
				("Field", "allant_a"),
				("Field", "venant_de"),
			)
		]

class LoginForm(forms.Form):
	identifiant = forms.CharField(max_length= 20)
	password = forms.CharField(max_length=20, widget= forms.PasswordInput())

class ContactForm(forms.ModelForm):
	class Meta:
		fields = '__all__'
		model = Message
		layout = [
			("Text", "<h3 class=\"ui dividing header left aligned\">Contactez-nous</h3>"),
			("Field", "nom"),
			("Field",'email'),
			("Field", 'contenu'),
		]        

	   
