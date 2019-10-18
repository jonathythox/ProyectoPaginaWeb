from django.db import models
from django.urls import reverse 
import uuid 


class Marca(models.Model):
	marca = models.CharField(max_length=200)
	
	def __str__(self):
		return self.marca


class Telefono(models.Model):
	nombre = models.CharField(max_length=200)
	marca = models.ManyToManyField(Marca)
	ram = models.CharField(max_length=4)
	descripcion = models.TextField(max_length=1000, help_text='Ingrese una descripcion sobre el telefono')

	def __str__(self):
		return self.id


class TelefonoInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico para el celular')
	telefono = models.ForeignKey('Telefono', on_delete=models.SET_NULL, null=True)
	compañia = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('a', 'Agotado'),
		('d', 'Disponible'),
		('r', 'rebajado'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Estado del libro',
	)

	class Meta:
		ordering = ['due_back']

	def __str__(self):
		return f'{self.id} ({self.telefono.nombre})'

