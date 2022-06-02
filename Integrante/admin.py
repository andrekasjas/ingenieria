from django.contrib import admin
from .models import *

# Register your models here.

# class tipo_integrante_admin(admin.ModelAdmin):
#     readonly_fields = ("created","updated")

class integrante_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
 



# admin.site.register(tipo_integrante, tipo_integrante_admin)
admin.site.register(integrante, integrante_admin)