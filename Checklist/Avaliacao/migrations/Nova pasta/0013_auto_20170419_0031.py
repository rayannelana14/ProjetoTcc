# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Avaliacao', '0012_auto_20170419_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='selectCat',
        ),
        migrations.AddField(
            model_name='checklist',
            name='selectCat',
            field=models.ForeignKey(default=(1, 2), on_delete=django.db.models.deletion.CASCADE, to='Avaliacao.Categoria'),
            preserve_default=False,
        ),
    ]
