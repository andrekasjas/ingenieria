from django.shortcuts import render, redirect

from Integrante.models import integrante
from .models import archivo
from Login.models import equipo
from .forms import Formulario_archivos
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required
def archivos(request, equipo_id):
    archivoss = archivo.objects.filter(equipo = equipo_id)
    return render(request, 'archivo/archivo.html',{'archivoss':archivoss, 'equipo':equipo_id})


def agregar_archivo(request, equipo_id):
    hola = equipo.objects.filter(id = equipo_id)
    for i in hola:
        holas = i
    if (request.method == "POST"):
        formulario = Formulario_archivos(request.POST, request.FILES)
        if (formulario.is_valid()):
            tarea = formulario.cleaned_data.get('tarea')
            tipo = formulario.cleaned_data.get('tipo')
            autorr = formulario.cleaned_data.get('autor')
            autors = integrante.objects.filter(id = autorr)
            for a in autors:
                autor = a
            estado = formulario.cleaned_data.get('estado')
            archivoc = request.FILES["url_archivo"]
            # handle_uploaded_file(archivo)
            url_archivo =  'archivos/'+archivoc.name
            add = archivo.objects.create(nombre=url_archivo, tarea=tarea, tipo=tipo, equipo=holas, autor=autor, estado=estado)
            add.save()

            try:
                
                return redirect('/equipos')
            except:
                return redirect('/archivo/agregar_archivo/'+str(equipo_id)+'/?novalido')
    else:
        formulario = Formulario_archivos()

    return render(request, "archivo/agregar_archivo.html",{'formulario':formulario})


def handle_uploaded_file(f):  
    with open('media/archivos/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  