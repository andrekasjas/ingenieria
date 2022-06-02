from django.urls import path
from .views import *


urlpatterns = [
    path('', agregar_integrante, name="agregar_integrante"),
]