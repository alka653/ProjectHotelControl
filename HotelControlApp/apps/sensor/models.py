from HotelControlApp.apps.principal.models import *
from HotelControlApp.apps.area.models import *
from django.db import models

class Sensor(models.Model):
	identificacion_sensor = models.CharField(max_length = 10)
	tipo_sensor = models.ForeignKey(TipoSensor)
	descripcion_sensor = models.CharField(max_length = 150)
	estado_sensor = models.ForeignKey(Estado)
	area = models.ForeignKey(Area)

	def __str__(self):
		return self.identificacion_sensor

	def __unicode__(self):
		return self.identificacion_sensor

class AreaSensorMedida(models.Model):
	area_sensor = models.ForeignKey(Sensor)
	medida_sensor = models.DecimalField(max_digits = 5, decimal_places = 2)
	fecha_medida_sensor = models.DateTimeField(auto_now = True)

	def __str__(self):
		return str(self.nombre_area) + " - " + str(self.medida_sensor)

	def __unicode__(self):
		return str(self.nombre_area) + " - " + str(self.medida_sensor)