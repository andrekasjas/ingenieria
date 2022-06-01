from django.contrib import admin
from .models import *

# Register your models here.
# class tipo_archivo_admin(admin.ModelAdmin):
#     readonly_fields = ("created","updated")

class archivo_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
# admin.site.register(tipo_archivo, tipo_archivo_admin)
admin.site.register(archivo, archivo_admin)