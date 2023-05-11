from django.db import models

# Create your models here.

class Malla(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    talle = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre} | {self.talle} | {self.precio}"
    
class Vestidos(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    talle = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre} | {self.talle} | {self.precio}"
    
class Sombreros(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    talle = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre} | {self.talle} | {self.precio}"

class Comprador(models.Model):
    nombre = models.CharField(max_length=256)
    apellido =models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    telefono = models.CharField(max_length=256)
    direccion = models.TextField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    telefono = models.CharField(max_length=256)
    direccion = models.TextField()
    redes = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre}"
