from django.db import models

# Create your models here.
from django.db import models

CATEGORIA_CHOICES = (
		('ESPECIALISTA', 'Especialista'),
		('AVALIADOR', 'Avaliador')
)
class Usuario(models.Model):	
	first_name = models.CharField(
		max_length=255,
	)
	last_name = models.CharField(
		max_length=255,
	)	
	email = models.EmailField()
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