from django.db import models

class Modelo1(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Modelo2(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    contenido = models.TextField()

class Modelo3(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    cantidad = models.PositiveIntegerField()