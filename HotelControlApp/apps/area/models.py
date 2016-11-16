from HotelControlApp.apps.principal.models import *
from django.db import models

class Area(models.Model):
	nombre_area = models.CharField(max_length = 45)
	descripcion_area = models.CharField(max_length = 150)
	estado_area = models.ForeignKey(Estado)

	def __str__(self):
		return self.nombre_area

	def __unicode__(self):
		return self.nombre_area