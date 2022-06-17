from django.db import models
from Login.models import equipo
from Login.models import integrante

# Create your models here. 
    
class archivo(models.Model):
    nombre = models.FileField(upload_to = 'archivos/', null = True, blank = True)
    tarea = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    equipo = models.ForeignKey(equipo, on_delete= models.CASCADE, default="")
    autor = models.ForeignKey(integrante, on_delete= models.CASCADE, default="")
    estado = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'archivos'
        verbose_name_plural = 'archivo'

    def __str__(self):
        return self.tarea