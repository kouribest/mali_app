# -*- coding: utf-8 -*

from django import forms
from mali_project.forms import FormBase

from rdc.models import RDCModel

ICON_GENRE= (
	("Homme", "Homme|man"),
	("Femme", "Femme|woman"),
)

RADIO_CHOICES = (
	("Oui","Oui"),
	("Non","Non")
)


class FormRDC(FormBase):
	perte_appetit= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Manque d'appétit ?") 
	fatigue_intense= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Une intense fatigue ?" ) 
	douleur_musculaire= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Des douleurs musculaires ?") 
	respiration_difficile= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label='Une respiration difficile ?' ) 
	douleur_abdominale= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Des douleurs abdominales ?" )
	difficulte_avaler= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect,  label="Des difficultés à avaler ?")
	yeux_rouge= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect,  label="Des yeux rouges ?")
	saignement_inexplique= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Des saignements inexpliqués ?")
	deces_inexplique= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Un decès inexplique est-il survenu ?")
	temperature_depart= forms.FloatField(max_value=45, min_value= 27, widget=forms.NumberInput(attrs={'step':'0.1'}))
	temperature_arrive= forms.FloatField(max_value=45, min_value= 27, widget=forms.NumberInput(attrs={'step':'0.1'}))

	class Meta(FormBase.Meta):
		model= RDCModel
		fields='__all__'
		exclude= ('etat',)
		layout=[
			("Field", "domain"),
			("Text", "<h3 class=\"ui dividing header left aligned\">Identite du voyageur (Traveller's Identity)</h3>"),
			("Field","identifiant"),
			("Three Fields",
				("Field","genre"),
				("Field","nom_famille"),
				("Field","prenom"),                
			),
			("Four Fields",
				("Field","numero_passport"),
				("Field","adresse_locale"),
				("Field","telephone"),
				("Field","date_naissance"),
			),
			("Text", "<h3 class=\"ui dividing header left aligned\">Informations sur le voyage (Travel's Informations)</h3>"),
			("Two Fields",
				("Field", "type_voyage"),
				("Field", "date_voyage"),               
			 ),
			("Field", "allant_a"),
			("Field", "venant_de"),

			("Text", "<div class='Vol_block'>"),
			("Two Fields",
				 ("Field","numero_siege"),
				 ("Field","numero_vol"),
			),
			("Text", "</div>"),

			("Text", "<div class='Voiture_block' style='display: none'>"),
			("Two Fields",
				("Field","nom_compagnie"),
				("Field","numero_matricule"),
			),
			("Text", "</div>"),

			("Text", "<div class='Navire_block' style='display: none'>"),
			("Two Fields",
				("Field","nom_bateau"),
				("Field","numero_cabine"),
			),
			("Text", "</div>"),
			("Text", "<h3 class=\"ui dividing header left aligned\">Informations sur la sante du voyage (Traveller's Health Informations</h3>"),
			("Four Fields",
				("Field", "perte_appetit"),              
				("Field", "fatigue_intense"),
				("Field", "douleur_musculaire"),
				("Field", "respiration_difficile"),
			 ),
			("Four Fields",
				("Field", "douleur_abdominale"),              
				("Field", "difficulte_avaler"),
				("Field", "yeux_rouge"),
			 ),
			("Two Fields",
				("Field", "deces_inexplique"),          
				("Field", "saignement_inexplique"),
			 ),
			("Two Fields",
				("Field", "temperature_arrive"),
				("Field", "temperature_depart"),
			 ),
		]

class FormAdminCongo(FormRDC):
	saignement_inexplique_agent= forms.ChoiceField(choices= RADIO_CHOICES, widget= forms.RadioSelect, label="Des saignements inexpliqués (agent) ?")
	class Meta(FormRDC.Meta):
		layout= FormRDC.Meta.layout + [
			('Text','<h3 class="ui dividing header left aligned">Zone reservee au personnel (Reserved for The Officer)</h3>'),
			("Field", "saignement_inexplique_agent"),
 			('Field', 'decision_officier')
 		]

	# def clean_motif_voyage(self):
	# 	value= self.cleaned_data['motif_voyage']
	# 	data_cleaned= ' '.join([str(c) for c in value])
	# 	return data_cleaned

	# def clean_hebergement(self):
	# 	value= self.cleaned_data['hebergement']
	# 	data_cleaned= ' '.join([str(c) for c in value])
	# 	return data_cleaned

