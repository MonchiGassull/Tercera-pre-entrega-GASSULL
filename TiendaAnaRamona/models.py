from django.db import models

# Create your models here.

class Malla(models.Model):
    nombre = models.CharField(max_length=256) #equivalente de str
    precio = models.IntegerField() #equivalente de int
    talle = models.CharField(max_length=256)
    
class Vestidos(models.Model):
    nombre = models.CharField(max_length=256) #equivalente de str
    precio = models.IntegerField() #equivalente de int
    talle = models.CharField(max_length=256)

class Comprador(models.Model):
    nombre = models.CharField(max_length=256)
    apellido =models.CharField(max_length=256)
    email=models.EmailField(max_length=256) # equivalente a email
    telefono = models.CharField(max_length=256)
    direccion = models.TextField()
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=256)
    email=models.EmailField(max_length=256) # equivalente a email
    telefono = models.CharField(max_length=256)
    direccion = models.TextField()
    redes = models.CharField(max_length=256)
