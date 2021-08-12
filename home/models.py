from django.db import models

class Student(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(max_length=255)

def __str__(self):
	return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=50)
