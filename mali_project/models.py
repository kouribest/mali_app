# -*- coding: utf-8 -*
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse 
from django.http.request import split_domain_port
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries import countries
from django.contrib import admin
from mali_project.settings import STATIC_ROOT
import string, random
import os, qrcode


COUNTRY=[(y, y) for x,y in countries.countries.items()]

DOMAINS_CACHE = {}
STATE=(
	(u"Invalide",u"Non valide"),
	(u"Valide",u"Valide"),	
)

GENRE = (
	(u"Homme", u"Homme"),
	(u"Femme", u"Femme"),
)


class DomainManager(models.Manager):
	use_in_migrations = True

	def _get_domain_by_id(self, domain_id):
		if domain_id not in DOMAINS_CACHE:
			domain = self.get(pk=domain_id)
			DOMAINS_CACHE[domain_id] = domain
		return DOMAINS_CACHE[domain_id]

	def _get_domain_by_request(self, request):
		host = request.get_host()
		try:
			if host not in DOMAINS_CACHE:
				DOMAINS_CACHE[host] = self.get(domain__iexact=host)
			return DOMAINS_CACHE[host]
		except Domain.DoesNotExist:
			domain, port = split_domain_port(host)
			if domain not in DOMAINS_CACHE:
				DOMAINS_CACHE[domain] = self.get(domain__iexact=domain)
			return DOMAINS_CACHE[domain]

	def get_current(self, request=None, domain_id=None):
		if domain_id:
			return self._get_domain_by_id(domain_id)
		elif request:
			return self._get_domain_by_request(request)

	def clear_cache(self):
		global DOMAINS_CACHE
		DOMAINS_CACHE = {}

	def get_by_natural_key(self, domain):
		return self.get(domain=domain)


class Domain(models.Model):
	# To use de custom Manager for this model
	domain = models.CharField(max_length=128, primary_key=True)
	name = models.CharField(max_length=10)
	owner = models.ForeignKey(User)
	objects = DomainManager()

	def __unicode__(self):
		return u'%s' % self.name

def randomStringDigits(stringLength=6, cache=None):
    """Generate a random string of letters and digits
       Check if there's a subclass which has already the generated to avoid collision
    """
    lettersAndDigits = string.ascii_uppercase + string.digits
    gen_string=''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    if cache and gen_string in cache:
    	return randomStringDigits(cache= cache)
    for subcls in BaseModel.__subclasses__():
    	if subcls.objects.filter(pk=gen_string).exists():
    		return randomStringDigits()
    cache.append(gen_string) if cache else False
    return gen_string

class BaseModel(models.Model):
	#Attached sub_domain
	domain = models.ForeignKey(Domain)
	identifiant = models.CharField(max_length=6, primary_key=True, default=randomStringDigits)

	venant_de = models.CharField(max_length = 50, choices= COUNTRY, verbose_name=u'Depart')
	allant_a = models.CharField(max_length = 50, choices= COUNTRY, verbose_name=u'Destination')

	#Common Field to all forms
	type_voyage = models.CharField(max_length = 20, blank = True)
	adresse_etranger = models.CharField(max_length = 50, blank = True, verbose_name=u"Adresse a l\'etranger")
	numero_vol = models.CharField(max_length = 7, blank = True, verbose_name=u'Numero du vol')
	numero_siege = models.CharField(max_length = 50, blank = True, verbose_name=u'Numero du siege'.encode('utf-8'))
	numero_cabine = models.CharField(max_length = 5, blank = True, verbose_name=u'Numero de la cabine')
	nom_bateau = models.CharField(max_length = 30, blank = True, verbose_name=u'Nom du bateau')
	numero_matricule = models.CharField(max_length = 50, blank = True, verbose_name=u'Immatriculation du vehicule')
	nom_compagnie = models.CharField(max_length=50, blank=True, verbose_name=u'Nom de la compagnie')
	nom_famille = models.CharField(max_length=50, verbose_name=u'Nom de famille')
	etat = models.CharField(max_length=30, choices= STATE, default='Invalide', verbose_name=u'Etat')
	numero_passport = models.CharField(max_length=50, verbose_name=u'Numero de passport')
	prenom = models.CharField(max_length=50, default="Neant")
	date_naissance = models.DateField(verbose_name=u'Date de naissance')
	genre = models.CharField(max_length=10, default="Homme", choices= GENRE )
	telephone = models.CharField(max_length=13)
	adresse_locale = models.CharField(max_length=50, blank= True, verbose_name=u'Adresse locale')
	date_voyage = models.DateTimeField(verbose_name=u'Date du voyage')
	date_enregistrement = models.DateField(auto_now=True, verbose_name=u'Date d\'enregistrement')

	class Meta:
		abstract = True

	def __str__(self):
		return u'{} - {} - {}'.format(self.nom_famille, self.prenom, self.identifiant)

	def get_absolute_url(self):
		return reverse('record_list')



class Message(models.Model):
	nom = models.CharField(max_length=30, verbose_name=u'Nom')
	email = models.EmailField()
	contenu= models.TextField()
