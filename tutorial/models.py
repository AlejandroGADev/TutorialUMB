from __future__ import unicode_literals

from django.db import models

class Alumnos(models.Model):
    nombre = models.CharField(max_length=230)
    apellido = models.CharField(max_length=230)
    domicilio = models.CharField(max_length=230)
    telefono = models.IntegerField()
