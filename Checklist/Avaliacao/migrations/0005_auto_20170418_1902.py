# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avaliacao', '0004_auto_20170418_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='data',
            field=models.CharField(max_length=80),
        ),
    ]
