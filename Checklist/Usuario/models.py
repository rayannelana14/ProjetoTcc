from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.template.defaultfilters import default

CATEGORIA_CHOICES = (
		('ESPECIALISTA', 'Especialista'),
		('AVALIADOR', 'Avaliador')
)
class Usuario(models.Model):	
	first_name = models.CharField(
		max_length=30, null = False
	)
	last_name = models.CharField(
		max_length=30, null = False
	)	
	email = models.EmailField(max_length = 80, null = False)
	categoria = models.CharField(
		max_length=18, 
		blank=True,
		choices=CATEGORIA_CHOICES,		
	)
	def __str__(self):
		return ' '.join([
			self.first_name,
			self.last_name,
		])