# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0005_auto_20170320_1451'),
        ('Avaliacao', '0003_auto_20170326_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=255, null=True)),
                ('data', models.DateTimeField()),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario')),				
            ],
        ),
        migrations.AddField(
            model_name='questao',
            name='diretrizes',
            field=models.CharField(max_length=255, null=True),
        ),
		
		migrations.AddField(
            model_name='Checklist',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Avaliacao.Categoria'),
            preserve_default=False,
        ),
    ]