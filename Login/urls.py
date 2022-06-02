from django.urls import path
from .views import *


urlpatterns = [
    path('registrar', registro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('equipos', equipos, name="equipos"),
    path('', logear, name="logear"),
    path('agregar_equipo',agregar_equipo, name="agregar_equipo")
]
