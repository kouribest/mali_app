from django.test import TestCase
from random import choice, randint
from mali.models import MaliModel as mali
from mali_project.models import randomStringDigits
from mali_project.models import Domain as dm
from datetime import datetime, timedelta
from django_countries import countries
from django.utils import timezone

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

def randomDate(start_date, end_date, output='datetime'):
	delta= (end_date - start_date)
	elapsed_second_delta= delta.total_seconds()
	new_date= start_date + timedelta(seconds=randint(3600*24, elapsed_second_delta))
	return (new_date if output == 'datetime' else new_date.date())

def SetUp(i):
	mali_list= []
	congo_list= []

	id_cache= [] #avoid duplicate collision 
	now= datetime.now(tz=timezone.utc)
	for i in range (1, i):
		mali_list.append(
			mali(
				identifiant= randomStringDigits(cache= id_cache),
				domain=dm.objects.first(),
				etat=choice(STATE)[0],
				type_voyage=choice(TYPE_VOYAGE)[0],
				numero_passport='B092289',
				prenom=choice(name_list),
				genre=choice(GENRE)[0],
				telephone='+3324834739',
				date_voyage=randomDate(now, now+timedelta(days=180)),
				date_enregistrement= randomDate(now, now+timedelta(days=365*10), 'date'),
				date_naissance= randomDate((now-timedelta(days=365*70)), now, 'date'),
				date_delivrance= randomDate(now, now+timedelta(days=180), 'date'),
				date_expiration= randomDate(now, now+timedelta(days=180), 'date'),
				venant_de= choice(countries.countries.keys()[0:10]),
				allant_a= choice(countries.countries.keys()[0:10]),
				autre_element=choice(OTHER_ELEMENT)[0],
				saignement_nez= choice(RADIO_CHOICES)[0],
				hebergement=choice(HEBERGEMENT)[0],
				motif_voyage=choice(MOTIF_VOYAGE)[0],
				premiere_visite= choice(RADIO_CHOICES)[0],
				fievre= choice(RADIO_CHOICES)[0],
				ecchymose= choice(RADIO_CHOICES)[0],
				contact_ebola= choice(RADIO_CHOICES)[0],
				cephale_douleur= choice(RADIO_CHOICES)[0],
				etablissement_ebola= choice(RADIO_CHOICES)[0],
			)
		)
		

	mali.objects.bulk_create(mali_list)


