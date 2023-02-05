from django.db import models
from django.contrib.auth.models import User
# from Integrante.models import integrante
# Create your models here.

class integrante(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'integrantes'
        verbose_name_plural = 'integrante'

    def __str__(self):
        return self.nombre


class equipo(models.Model):
    nombre = models.CharField(max_length=60)
    autor = models.ForeignKey(User, on_delete= models.CASCADE, default=User)
    integrante = models.ManyToManyField(integrante)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'

    def __str__(self):
        return self.nombre




