# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import mali_project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mali_project', '0008_auto_20190314_0016'),
        ('mali', '0018_auto_20190310_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaliModel',
            fields=[
                ('identifiant', models.CharField(default=mali_project.models.randomStringDigits, max_length=6, primary_key=True, serialize=False)),
                ('venant_de', django_countries.fields.CountryField(max_length=2)),
                ('allant_a', django_countries.fields.CountryField(max_length=2)),
                ('type_voyage', models.CharField(blank=True, max_length=20)),
                ('adresse_etranger', models.CharField(blank=True, max_length=50)),
                ('numero_vol', models.CharField(blank=True, max_length=7)),
                ('numero_siege', models.CharField(blank=True, max_length=50)),
                ('numero_cabine', models.CharField(blank=True, max_length=5)),
                ('nom_bateau', models.CharField(blank=True, max_length=30)),
                ('numero_matricule', models.CharField(blank=True, max_length=50)),
                ('nom_compagnie', models.CharField(blank=True, max_length=50)),
                ('nom_famille', models.CharField(max_length=50)),
                ('etat', models.CharField(choices=[('Invalide', 'Non valide'), ('Valide', 'Valide')], default=b'Invalide', max_length=30)),
                ('numero_passport', models.CharField(max_length=50)),
                ('prenom', models.CharField(default=b'Neant', max_length=50)),
                ('date_naissance', models.DateField()),
                ('genre', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default=b'Homme', max_length=10)),
                ('telephone', models.CharField(max_length=13)),
                ('adresse_locale', models.CharField(blank=True, max_length=50)),
                ('date_voyage', models.DateTimeField()),
                ('date_enregistrement', models.DateTimeField(auto_now=True)),
                ('passport_emis_par', models.CharField(blank=True, max_length=50)),
                ('date_delivrance', models.DateField()),
                ('date_expiration', models.DateField()),
                ('num_visa', models.CharField(blank=True, max_length=50)),
                ('visa_delivre_par', models.CharField(blank=True, max_length=20)),
                ('nationalite', models.CharField(blank=True, max_length=50)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('motif_voyage', models.CharField(max_length=100, verbose_name=b'Quel est le motif de votre voyage ?')),
                ('hebergement', models.CharField(max_length=100)),
                ('premiere_visite', models.CharField(default=b'Non', max_length=50)),
                ('fievre', models.CharField(default=b'Oui', max_length=30)),
                ('ecchymose', models.CharField(default=b'Non', max_length=30)),
                ('saignement_nez', models.CharField(default=b'Non', max_length=30)),
                ('contact_ebola', models.CharField(default=b'Non', max_length=30)),
                ('etablissement_ebola', models.CharField(default=b'Non', max_length=30)),
                ('lieu_naissance', models.CharField(default=b'Neant', max_length=50)),
                ('cephale_douleur', models.CharField(default=b'Non', max_length=13)),
                ('autre_element', models.CharField(max_length=55)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mali_project.Domain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
