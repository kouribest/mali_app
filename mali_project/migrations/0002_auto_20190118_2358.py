# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-18 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mali_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='cephale_douleur',
            field=models.CharField(default=b'Oui', max_length=30),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='contact_ebola',
            field=models.CharField(default=b'Oui', max_length=30),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='date_vol',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='diarrhee_vomissement',
            field=models.CharField(default=b'Oui', max_length=30),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='ecchymose',
            field=models.CharField(default=b'Oui', max_length=30),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='etablissement_ebola',
            field=models.CharField(default=b'Oui', max_length=30),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='fievre',
            field=models.CharField(default=b'Oui', max_length=30),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='genre',
            field=models.CharField(default=b'Homme', max_length=50),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='premiere_visite',
            field=models.CharField(default=b'Oui', max_length=50),
        ),
    ]
