# -*- coding: utf-8 -*
from django.db import models
from mali_project.models import BaseModel


class RDCModel(BaseModel):

    perte_appetit = models.CharField(max_length=30, blank=True)
    fatigue_intense = models.CharField(max_length=30, blank=True)
    douleur_musculaire = models.CharField(max_length=30, blank=True)
    respiration_difficile = models.CharField(max_length=30, blank=True, verbose_name="Des difficultés respiratoires ?")   
    douleur_abdominale = models.CharField(max_length=30, blank=True)
    difficulte_avaler = models.CharField(max_length=30, blank=True)   
    yeux_rouge = models.CharField(max_length=30, blank=True)   
    saignement_inexplique = models.CharField(max_length=30, blank=True)
    deces_inexplique = models.CharField(max_length=30, blank=True)   
    temperature_arrive = models.FloatField()   
    temperature_depart = models.FloatField()   
    saignement_inexpliqe_agent = models.CharField(max_length=30, blank=True)   
    decision_officier = models.TextField(blank=True) 

    class Meta:
        verbose_name = 'Formulaire Congolais'
        verbose_name_plural = 'Formulaires Congolais'
