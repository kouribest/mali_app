# -*- coding: utf-8 -*
from django import forms
from mali.models import MaliModel
from mali_project.forms import FormBase

ICON_GENRE= (
	("Homme", "Homme|man"),
	("Femme", "Femme|woman"),
)

OTHER_ELEMENT=(
	(u"Animaux",u"Animaux"),
	(u"Viande(poisson ou fruits de mer)",u"Viande(poisson ou fruits de mer)"),
	(u"Plantes(Legumes ou semences ou fruits ou fleurs)",u"Plantes(Legumes ou semences ou fruits ou fleurs)"),
	(u"Aucun",u"Aucun")
)

RADIO_CHOICES=(
	(u"Oui",u"Oui"),
	(u"Non",u"Non"),
)

HEBERGEMENT = [
	(u"Famille", u"Famille"),
	(u"Ami",u"Ami"),
	(u"Hotel",u"Hotel"),
	(u"Autre",u"Autre"),
]

MOTIF_VOYAGE = [
	(u"Affaire",u"Affaire"),
	(u"Congres",u"Congres"),
	(u"Vacances",u"Vacances"),
	(u"Loisir & Plaisir",u"Loisir & Plaisir"),
	(u"Visite Famille & Ami",u"Visite Famille & Ami"),
	(u"Religion & Pelerinage",u"Religion & Pelerinage"),
	(u"Culture",u"Culture"),
	(u"Recherche",u"Recherche"),
	(u"Autre",u"Autre"),
]

TYPE_VOYAGE =[
	('Vol','Vol|plane'),
	('Navire', 'Navire|anchor'),
	('Voiture', 'Voiture|car'),
	('Autre', 'Autre')
]



class FormML(FormBase):
	motif_voyage= forms.MultipleChoiceField(choices= MOTIF_VOYAGE, label= 'Quel est le motif de votre voyage ?')
	hebergement= forms.MultipleChoiceField(choices= HEBERGEMENT,  label= 'Où est-ce que vous serez hebergé ?')
	autre_element= forms.ChoiceField(choices=OTHER_ELEMENT, label= "Voyagez-vous avec l'un des elements suivants ?")
	saignement_nez= forms.ChoiceField(choices=RADIO_CHOICES, initial= 'Non', widget= forms.RadioSelect(), label="Saignement du nez")
	premiere_visite= forms.ChoiceField(label='Est-ce votre première visite ?', choices= RADIO_CHOICES, initial='Non', widget= forms.RadioSelect())
	fievre= forms.ChoiceField(choices= RADIO_CHOICES, initial='Non', widget= forms.RadioSelect(), label='Fièvre')
	diarrhee_vomissement= forms.ChoiceField(choices= RADIO_CHOICES, initial= 'Non', widget= forms.RadioSelect(), label='Vomissement ou Diarrhée')
	ecchymose= forms.ChoiceField(choices= RADIO_CHOICES, initial='Non', widget= forms.RadioSelect(), label='Ecchymose ou Saignement' )
	contact_ebola= forms.ChoiceField(choices= RADIO_CHOICES, initial='Non', widget= forms.RadioSelect(), label='En contact avec un malade Ebola')
	cephale_douleur= forms.ChoiceField(choices= RADIO_CHOICES, initial='Non', widget= forms.RadioSelect(), label='Maux de tête')
	etablissement_ebola= forms.ChoiceField(choices= RADIO_CHOICES, initial='Non', widget= forms.RadioSelect(), label='Frequentation d’un etablissement soignant les malades Ebola')
	
	
	class Meta(FormBase.Meta):
		model= MaliModel
		fields= '__all__'
		exclude= ('etat',)
		layout=[
			("Field", 'identifiant'),
			("Text", "<h3 class=\"ui dividing header left aligned\">Informations sur le vol</h3>"),
			("Two Fields",
				("Field","type_voyage"),
				("Field", "date_voyage"), 
			),

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

			("Field", "allant_a"),
			("Field", "venant_de"),
			 ("Three Fields",
					
				("Field","numero_siege"),
				
			),
			("Text", "<h3 class=\"ui dividing header left aligned\">Informations sur le titre de voyage</h3>"),
			("Four Fields",
				("Field","numero_passport"),
				("Field","date_delivrance"),
				("Field","date_expiration"),
				("Field", "passport_emis_par"),
			),
			("Two Fields",
				("Field", "num_visa"),
				("Field", "visa_delivre_par"), 
			),
			("Text", "<h3 class=\"ui dividing header left aligned\">Informations sur le voyageur</h3>"),
			("Four Fields",
				("Field","nom_famille"),
				("Field","prenom"),
				("Field","date_naissance"),
				("Field", "lieu_naissance"),
			),
			 ("Four Fields",
				("Field", "genre"),
				("Field", "nationalite"),
				("Field", "profession"),
				("Field", "telephone"),
			),
			 ("Three Fields",
				("Field", "email"),
				("Field", "adresse_locale"),
				("Field", "adresse_etranger"),
			),
			("Text", "<h3 class=\"ui dividing header left aligned\">Information sur le sejour</h3>"),
			("Three Fields",
				("Field", "premiere_visite"),
				("Field", "motif_voyage"),
				("Field", "hebergement"),   
			),
			("Text", "<h3 class=\"ui dividing header left aligned\">Information sanitaire</h3>"),
			("Text", "<h4 class=\"ui header left aligned\">Avez-vous ressenti aujourd'hui l'un des symptômes suivants ?</h4>"),
			("inline Fields",
				("Field", "fievre"),
				("Field", "diarrhee_vomissement"),
				("Field", "cephale_douleur"),
				("Field", "ecchymose"),
				("Field", "saignement_nez"),
				
			),
			("Text", "<h4 class=\"ui header left aligned\">Au cours des 3 dernières semaines, vous êtes-vous trouves dans l'une des situations suivantes ?</h4>"),
			("Two Fields",
				("Field", "contact_ebola"),
				("Field", "etablissement_ebola"),
			),
			("Text", "<h4 class=\"ui header left aligned\">Voyagez-vous avec l'un des elements suivants ?</h4>"),
			("Field", "autre_element"),
		]


	# def clean_motif_voyage(self):
	# 	value= self.cleaned_data['motif_voyage']
	# 	data_cleaned= ', '.join([str(c) for c in value])
	# 	return data_cleaned

	# def clean_hebergement(self):
	# 	value= self.cleaned_data['hebergement']
	# 	data_cleaned= ', '.join([str(c) for c in value])
	# 	return data_cleaned

