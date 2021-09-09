from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Company(models.Model):
	class Meta:
		verbose_name = 'Empresa'
		verbose_name_plural = 'Empresas'

	name = models.CharField(
		verbose_name='nombre',
		max_length=256
	)
	
	document = models.CharField(
		verbose_name='RUC/CI',
		max_length=20
	)

	telephone = models.CharField(
		verbose_name='telefono',
		max_length=20,
		null=True, 
		blank=True
	)

	cellphone = models.CharField(
		verbose_name='celular',
		max_length=20,
		null=True, 
		blank=True
	)

	address = models.TextField(
		verbose_name='direccion',
		null=True, 
		blank=True
	)

	def __str__(self):
		return self.name

class UserCompany(models.Model):
	class Meta:
		verbose_name = 'Usuario-Empresa'
		verbose_name_plural = 'Usuario-Empresa'

	user = models.ForeignKey(
		User,
		verbose_name='usuario', 
		on_delete=models.CASCADE, 
		related_name='+'
	)

	company = models.ForeignKey(
		Company, 
		verbose_name='empresa',
		on_delete=models.CASCADE, 
		related_name='+'
	)

	def __str__(self):
		return '%s %s' % ( self.user.get_short_name(), self.company.name )

class City(models.Model):
	class Meta:
		verbose_name = 'Ciudad'
		verbose_name_plural = 'Ciudades'

	name = models.CharField(
		verbose_name='nombre',
		max_length=256
	)

	service_amount = models.IntegerField(verbose_name='costo del servicio')
	employee_amount = models.IntegerField(verbose_name='comisión del gestor')
	aedo_amount = models.IntegerField(verbose_name='comisión AEDO')

	def __str__(self):
		return self.name


DELIVERY_STATUS = [
    (0, 'PENDIENTE'),
    (1, 'RETIRADO'),
    (2, 'EN CAMINO'),
    (3, 'ENTREGADO'),
    [4, 'CANCELADO']
]

FINANCIAL_STATE = [
	(0, 'PENDIENTE DE COBRO'),
	(1, 'PENDIENTE DE PAGO'),
	(2, 'RENDIDO')
]

class Delivery(models.Model):
	class Meta:
		verbose_name = "Entrega"
		verbose_name_plural = "Entregas"

	package = models.TextField(
		verbose_name="paquete",
		null=True,
		blank=True
	)

	company = models.ForeignKey(
		Company, 
		verbose_name='empresa',
		on_delete=models.CASCADE, 
		related_name='+'
	)

	employee = models.ForeignKey(
		User,
		verbose_name='gestor', 
		on_delete=models.CASCADE, 
		related_name='+',
		null=True,
		blank=True
	)

	city = models.ForeignKey(
		City,
		verbose_name='ciudad', 
		on_delete=models.CASCADE, 
		related_name='+'
	)

	origin_address = models.TextField(
		verbose_name='dirección de origen', 
		null=True, 
		blank=True
	)

	destination_address = models.TextField(
		verbose_name='dirección de destino', 
		null=True, 
		blank=True
	)

	reception_date = models.DateField(
		verbose_name='fecha de retiro',
		null=True,
		blank=True
	)

	reception_time = models.TimeField(
		verbose_name='hora de retiro',
		null=True,
		blank=True
	)

	deliver_date = models.DateField(
		verbose_name='fecha de entrega',
		null=True,
		blank=True
	)

	deliver_time = models.TimeField(
		verbose_name='hora de entrega',
		null=True,
		blank=True
	)

	service_amount = models.IntegerField(verbose_name='costo del servicio')
	employee_amount = models.IntegerField(verbose_name='comisión del gestor')
	aedo_amount = models.IntegerField(verbose_name='comisión AEDO')
	company_amount = models.IntegerField(verbose_name='comisión de la empresa')

	state = models.PositiveSmallIntegerField(
		verbose_name='estado de la encomienda',
		choices=DELIVERY_STATUS, 
		default=0
	)

	state2 = models.PositiveSmallIntegerField(
		verbose_name='estado de la operación',
		choices=FINANCIAL_STATE, 
		default=0
	)

	comment = models.TextField(
		verbose_name='observaciones',
		null=True,
		blank=True
	)

	received = models.IntegerField(verbose_name='cobrado', default=0)

	def get_total(self):
		return self.service_amount + self.company_amount

	def get_pending(self):
		return self.service_amount + self.company_amount - self.received

	def __str__(self):
		return "Entrega ID: " + str(self.id)


class Service(models.Model):
	class Meta:
		verbose_name = "Servicio"
		verbose_name_plural = "Servicios"

	description = models.TextField()

	def __str__(self):
		return self.description