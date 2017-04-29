from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import default
from Usuario.models import Usuario
from Sistema.models import Sistema
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

class Avaliacao(models.Model):
	sistema = models.ForeignKey(Sistema)
	nome = models.CharField(max_length = 80, null =False)
	responsavel = models.ManyToManyField(Usuario, through='Avaliacao_Responsavel')
	plataforma = models.CharField(max_length = 80, null=False)
	checklist = models.ForeignKey(Checklist)

class Avaliacao_Responsavel(models.Model):
	avaliacao = models.ForeignKey(Avaliacao)
	responsavel = models.ForeignKey(Usuario)

class Resposta(models.Model):
	questao = models.ForeignKey(Questoes)
	resposta = models.CharField(max_length = 3, null= False)
	avaliacao = models.ForeignKey(Avaliacao)
	checklist = models.ForeignKey(Checklist)
