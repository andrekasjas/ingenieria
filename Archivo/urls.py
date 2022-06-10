from django.urls import path
from .views import *


urlpatterns = [
    path('<int:equipo_id>/', archivos, name="archivo"),
    path('agregar_archivo/<int:equipo_id>/', agregar_archivo, name="agregar_archivo"),
]