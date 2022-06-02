from django.shortcuts import render, redirect
from .forms import Formulario_integrante
from .models import integrante
# Create your views here.

def agregar_integrante(request):
    if (request.method == "POST"):
        formulario = Formulario_integrante(data = request.POST)
        if (formulario.is_valid()):
            nombre = formulario.cleaned_data.get('nombre')
            tipo = formulario.cleaned_data.get('tipo') 

            try:
                add = integrante.objects.create(nombre = nombre, tipo = tipo)
                add.save()
                return redirect('/equipos')
            except:
                return redirect('/integrante/?novalido')
    else:
        formulario = Formulario_integrante()

    return render(request, "integrante/agregar_integrante.html",{'formulario':formulario})