from django.shortcuts import render, redirect
from .models import archivo
from Login.models import equipo
from .forms import formulario_equipo, Formulario_archivos, Formulario_editar, Formulario_editar_estado
from django.contrib.auth.decorators import login_required
import cloudinary

@login_required
def archivos(request, equipo_id):
    archivoss = archivo.objects.filter(equipo = equipo_id).order_by('-estado')
    return render(request, 'archivo/archivo.html',{'archivoss':archivoss, 'equipo':equipo_id})


def agregar_archivo(request, equipo_id):
    equipos = equipo.objects.get(id = equipo_id)
    # for i in equipos:
    #     equi = i
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
            add = archivo.objects.create(nombre=archivoc, tarea=tarea, tipo=tipo, equipo=equipos, autor=autor, estado=estado)
            add.save()

            try:
                
                return redirect('/archivo/{}'.format(str(equipo_id)))
            except:
                return redirect('/archivo/agregar_archivo/'+str(equipo_id)+'/?novalido')
    else:
        formulario = formulario_equipo(equipo_id)

    return render(request, "archivo/agregar_archivo.html",{'formulario':formulario})

def editar_estado(request, equipo_id, archivo_id):
    archivos = archivo.objects.get(id = archivo_id)
    if (request.method == "POST"):
        formulario = Formulario_editar_estado(request.POST, request.FILES)
        if (formulario.is_valid()):
            estado = formulario.cleaned_data.get('estado')
            archivoc = request.FILES["url_archivo"]
            
            cloudinary.uploader.destroy(str(archivos.nombre))
            archivos.estado = estado
            archivos.nombre = archivoc
            archivos.save()

            try:              
                return redirect('/archivo/{}'.format(str(equipo_id)))
            except ValueError:
                print(ValueError)
                return redirect('/archivo/editar_estado/{}/{}/?novalido'.format(str(equipo_id),str(archivo_id)))
    else:
        formulario = Formulario_editar(archivos.estado)

    return render(request, "archivo/editar_estado.html",{'formulario':formulario})



# def handle_uploaded_file(f):  
#     with open('https://res.cloudinary.com/dc1hb2uev/image/upload/v1/ingenieria/archivos/'+f.name, 'wb+') as destination:  
#         for chunk in f.chunks():
#             destination.write(chunk)  