# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-09 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mali_project', '0005_auto_20190201_0348'),
        ('mali', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaliModel',
            fields=[
                ('identifiant', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('venant_de', django_countries.fields.CountryField(max_length=2)),
                ('allant_a', django_countries.fields.CountryField(max_length=2)),
                ('adresse_etranger', models.CharField(blank=True, max_length=50)),
                ('numero_voyage', models.CharField(blank=True, max_length=7)),
                ('numero_siege', models.CharField(blank=True, max_length=50)),
                ('nom_famille', models.CharField(max_length=50)),
                ('numero_passport', models.CharField(max_length=50)),
                ('prenom', models.CharField(default=b'Neant', max_length=50)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(default=b'Neant', max_length=50)),
                ('genre', models.CharField(default=b'Homme', max_length=50)),
                ('telephone', models.CharField(default=b'Neant', max_length=13)),
                ('adresse_locale', models.CharField(default=b'Neant', max_length=50)),
                ('fievre', models.CharField(default=b'Oui', max_length=30)),
                ('cephale_douleur', models.CharField(default=b'Non', max_length=13)),
                ('date_voyage', models.DateTimeField()),
                ('passport_emis_par', models.CharField(default=b'Police', max_length=50)),
                ('date_delivrance', models.DateField()),
                ('date_expiration', models.DateField()),
                ('num_visa', models.CharField(default=b'N/C', max_length=50)),
                ('visa_delivre_par', models.CharField(default=b'N/C', max_length=20)),
                ('nationalite', models.CharField(blank=True, max_length=50)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('motif_voyage', models.CharField(max_length=100)),
                ('hebergement', models.CharField(max_length=100)),
                ('premiere_visite', models.CharField(default=b'Oui', max_length=50)),
                ('ecchymose', models.CharField(default=b'Oui', max_length=30)),
                ('contact_ebola', models.CharField(default=b'Oui', max_length=30)),
                ('etablissement_ebola', models.CharField(default=b'Oui', max_length=30)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mali_project.Domain')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='ml_form_model',
            name='domain',
        ),
        migrations.DeleteModel(
            name='ml_form_model',
        ),
    ]
