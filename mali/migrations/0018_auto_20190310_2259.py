# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-10 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mali', '0017_malimodel_etat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='malimodel',
            name='domain',
        ),
        migrations.DeleteModel(
            name='MaliModel',
        ),
    ]
