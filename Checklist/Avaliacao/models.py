from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import default
from Usuario.models import Usuario
# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(
		max_length=150, null = False, unique=True
	)
	descricao = models.CharField(
		max_length=180, null = False
	)

class Questoes(models.Model):
	questao = models.CharField(
		max_length = 255, null = False
	)
	Categoria = models.ForeignKey(Categoria)
	diretrizes = models.CharField(
		max_length = 255, null = True
	)

class Checklist(models.Model):
	nome = models.CharField(
		max_length = 80, null=False, unique=True
	)
	descricao = models.CharField(
		max_length = 255, null= True
	)
	especialista = models.ForeignKey(Usuario)	
	categoria = models.ManyToManyField(Categoria, through='Checklist_Categoria')

class Checklist_Categoria(models.Model):
	checklist = models.ForeignKey(Checklist)
	categoria = models.ForeignKey(Categoria)

	


	
