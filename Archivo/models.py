from django.db import models
from Login.models import equipo
from Integrante.models import integrante

# Create your models here.

# class tipo_archivo(models.Model):
#     nombre = models.CharField(max_length=60)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'tipos archivos'
#         verbose_name_plural = 'tipo archivo'

#     def __str__(self):
#         return self.nombre
    
class archivo(models.Model):
    nombre = models.FileField(upload_to = 'archivos/', null = True, blank = True)
    tarea = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    equipo = models.ForeignKey(equipo, on_delete= models.CASCADE, default="")
    autor = models.ForeignKey(integrante, on_delete= models.CASCADE, default="")
    estado = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'archivos'
        verbose_name_plural = 'archivo'

    def __str__(self):
        return self.tarea