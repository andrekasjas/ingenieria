from django.shortcuts import render, redirect


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
            autor = formulario.cleaned_data.get('autor')
            estado = formulario.cleaned_data.get('estado')
            archivoc = request.FILES["url_archivo"]
            #handle_uploaded_file(archivoc)
            #url_archivo =  'static/archivos/'+archivoc.name
            add = archivo.objects.create(nombre=archivoc, tarea=tarea, tipo=tipo, equipo=holas, autor=autor, estado=estado)
            add.save()

            try:
                
                return redirect('/archivo/{}'.format(equipo_id))
            except:
                return redirect('/archivo/agregar_archivo/'+str(equipo_id)+'/?novalido')
    else:
        formulario = Formulario_archivos()

    return render(request, "archivo/agregar_archivo.html",{'formulario':formulario})


# def handle_uploaded_file(f):  
#     with open('https://res.cloudinary.com/dc1hb2uev/image/upload/v1/ingenieria/archivos/'+f.name, 'wb+') as destination:  
#         for chunk in f.chunks():
#             destination.write(chunk)  