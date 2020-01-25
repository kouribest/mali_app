from django.test import TestCase
from random import choice, randint
from mali.models import MaliModel as mali
from mali.forms import FormML
from mali_project.models import Domain as dm, randomStringDigits
from datetime import datetime, timedelta, tzinfo
from django_countries import countries
from django.utils import timezone
from django.forms.models import model_to_dict
from django.test import Client
import requests, json

STATE=(
	(u"Invalide",u"Non valide"),
	(u"Valide",u"Valide"),	
)

GENRE = (
	(u"Homme", u"Homme"),
	(u"Femme", u"Femme"),
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

TYPE_VOYAGE=(
	('Vol','Vol|plane'),
	('Navire', 'Navire|anchor'),
	('Voiture', 'Voiture|car'),
	('Autre', 'Autre')
)

name_list= [
	"Rosalba",
	"Florentina",
	"Erminia",
	"Markus",
	"An",
	"Enoch",
	"Sheryl",
	"Jalisa",
	"Estelle",
	"Elin",
	"Nancy",
	"Cyrus",
	"Loretta",
	"Tomas",
	"Ashli",
	"Lucille",
	"Darryl",
	"Andreas",
	"Minerva",
	"Marion",
	"Marketta",
	"Jammie",
	"Antoine",
	"Kimbra",
	"Classie",
	"Ciera",
	"Mora",
	"Tyler",
	"Tonia",
	"Eduardo",
	"Sharla",
	"Bernita",
	"Nathan",
	"Valentina",
	"Tammy",
	"Ali",
	"Mireille",
	"Luana",
	"Creola",
	"Adelle",
	"Russel",
	"Hillary",
	"Rosaline",
	"Amber",
	"Tiffiny",
	"Shanda",
	"Emmett",
	"Song",
	"Karrie",
	"Joset",  
]

id_cache = []

def randomDate(start_date, end_date, output='datetime'):
	delta = (end_date - start_date)
	elapsed_second_delta = delta.total_seconds()
	print(elapsed_second_delta)
	new_date = start_date + timedelta(seconds=randint(3600*24, elapsed_second_delta))
	return (new_date if output == 'datetime' else new_date.date())


class TestRecord(TestCase):

	def setUp(self):
		mali_list= []
		congo_list= []
		now = datetime.now()

		self.client = Client()

		self.obj = mali(
			identifiant= randomStringDigits(cache= id_cache),
			etat=choice(STATE)[0],
			type_voyage=choice(TYPE_VOYAGE)[0],
			numero_passport='B0XXXX',
			prenom=choice(name_list),
			nom_famille=choice(name_list),
			genre=choice(GENRE)[0],
			telephone='+33xxxxxx',
			date_voyage=randomDate(now, now + timedelta(days=180)),
			date_enregistrement= randomDate(now, now + timedelta(days=365*10), 'date'),
			date_naissance=randomDate((now - timedelta(days=365*70)), now, 'date'),
			date_delivrance=randomDate(now, now + timedelta(days=180), 'date'),
			date_expiration=randomDate(now, now + timedelta(days=180), 'date'),
			venant_de=list(countries.countries.values()).pop(2),
			allant_a=list(countries.countries.values()).pop(),
			autre_element=choice(OTHER_ELEMENT)[0],
			saignement_nez=choice(RADIO_CHOICES)[0],
			hebergement=choice(HEBERGEMENT),
			motif_voyage=choice(MOTIF_VOYAGE),
			premiere_visite=choice(RADIO_CHOICES)[0],
			fievre=choice(RADIO_CHOICES)[0],
			diarrhee_vomissement=choice(RADIO_CHOICES)[0],
			ecchymose=choice(RADIO_CHOICES)[0],
			contact_ebola=choice(RADIO_CHOICES)[0],
			cephale_douleur=choice(RADIO_CHOICES)[0],
			etablissement_ebola=choice(RADIO_CHOICES)[0],
		)

	def test_valid_mali_form(self):
		data = model_to_dict(self.obj)
		form = FormML(data)
		self.assertEqual(form.is_valid(), True)


	def test_invalid_travel_date(self):
		now = datetime.now()
		self.obj.date_voyage = randomDate(now - timedelta(days=4), now - timedelta(days=1))
		data = model_to_dict(self.obj)
		form = FormML(data)

		self.assertEqual(form.is_valid(), False)
