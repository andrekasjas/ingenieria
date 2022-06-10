from django.db import models
# Create your models here.

# class tipo_integrante(models.Model):
#     nombre = models.CharField(max_length=60)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'tipos integrante'
#         verbose_name_plural = 'tipo integrante'

#     def __str__(self):
#         return self.nombre

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
