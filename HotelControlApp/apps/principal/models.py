from django.db import models

class TipoSensor(models.Model):
	nombre_tipo_sensor = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre_tipo_sensor

	def __unicode__(self):
		return self.nombre_tipo_sensor

class Estado(models.Model):
	nombre_estado = models.CharField(max_length = 45)

	def __str__(self):
		return self.nombre_estado

	def __unicode__(self):
		return self.nombre_estado