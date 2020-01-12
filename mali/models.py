 # -*- coding: utf-8 -*
from __future__ import unicode_literals
from django.db import models
from mali_project.models import BaseModel
from django.contrib import admin
from datetime import datetime



class MaliModel(BaseModel):
	
	passport_emis_par = models.CharField(max_length=50, blank=True, verbose_name=u'Lieu d\'etablissement')
	date_delivrance = models.DateField(verbose_name= u'Date de delivrance' )
	date_expiration = models.DateField(verbose_name= u'Date d\'expiration')
	num_visa = models.CharField(max_length=50, blank=True, verbose_name= u'Numero du VISA')
	visa_delivre_par = models.CharField(max_length=20, blank=True, verbose_name=u'Ou avez-vous obtenu votre Visa ?')

	nationalite = models.CharField(max_length=50, blank=True)
	profession = models.CharField(max_length=50, blank=True)
	email = models.CharField(max_length=50, blank=True)

	motif_voyage = models.CharField(max_length=100,  blank=False, verbose_name=u'Quel est le motif de votre voyage ?')
	hebergement = models.CharField(max_length=100,  blank=False)
	premiere_visite = models.CharField(max_length=50, default="Non", blank= False )
	fievre = models.CharField(max_length=30, default="Oui", blank=False)
	ecchymose = models.CharField(max_length=30, default="Non", blank= False)
	saignement_nez = models.CharField(max_length=30, default="Non", blank= False)
	contact_ebola = models.CharField(max_length=30, default="Non", blank= False)
	etablissement_ebola = models.CharField(max_length=30, default="Non", blank= False)
	diarrhee_vomissement = models.CharField(max_length=30, default="Non", blank= False)
	lieu_naissance = models.CharField(max_length=50, default="Neant")
	cephale_douleur = models.CharField(max_length=13, default="Non")
	autre_element = models.CharField(max_length=55, blank=False)


	class Meta:
		verbose_name= 'Formulaire Malien'
		verbose_name_plural = 'Formulaires Maliens'
	


	

	


		
