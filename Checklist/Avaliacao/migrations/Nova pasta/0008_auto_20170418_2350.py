# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 02:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avaliacao', '0007_checklist_categorias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='categorias',
            new_name='categoria',
        ),
    ]