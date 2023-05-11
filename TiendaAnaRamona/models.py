from django.db import models

# Create your models here.

class Malla(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    talle = models.CharField(max_length=256)
    
class Vestidos(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    talle = models.CharField(max_length=256)
    
class Sombreros(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    talle = models.CharField(max_length=256)

class Comprador(models.Model):
    nombre = models.CharField(max_length=256)
    apellido =models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    telefono = models.CharField(max_length=256)
    direccion = models.TextField()
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    telefono = models.CharField(max_length=256)
    direccion = models.TextField()
    redes = models.CharField(max_length=256)
