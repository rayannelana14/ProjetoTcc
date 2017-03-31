from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import default
# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(
		max_length=150, null = False, unique=True
	)
	descricao = models.CharField(
		max_length=180, null = False
	)

class Questao(models.Model):
	questao = models.CharField(
		max_length = 255, null = False
	)
	Categoria = models.ForeignKey('Categoria')
		
