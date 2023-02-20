from django.db import models
from .validators import validar_cuatro_cifras, validar_no_cero

class Camion(models.Model):
    marca = models.CharField(max_length=10)
    capacidad = models.DecimalField(decimal_places=2, max_digits=6, validators=[validar_cuatro_cifras])
    modelo = models.CharField(max_length=4)
    placa = models.CharField(max_length=7)

    def __str__(self):
        return self.marca

class Conductor(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombres} - {self.apellidos}"
    
class Viaje(models.Model):
    origen = models.TextField()
    destino = models.TextField()
    
class Gastos(models.Model):
    combustible = models.DecimalField(decimal_places=2, max_digits=5,validators=[validar_no_cero])
    viaticos = models.DecimalField(decimal_places=2, max_digits=5)
    peajes= models.DecimalField(decimal_places=2, max_digits=5,validators=[validar_no_cero])