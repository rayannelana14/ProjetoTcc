from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.template.defaultfilters import default

class Sistema(models.Model):
	requisitos = models.CharField(
		max_length=100, null = True
	)
	metas = models.DecimalField(
		max_digits=5, decimal_places=2
	)
	categoria = models.CharField(
		max_length=30, null= False
	)
	nome = models.CharField(
		max_length=50, null=False
	)
	empresa = models.CharField(
		max_length=50, null=False
	)
	projeto = models.CharField(
		max_length=50, null=True
	)