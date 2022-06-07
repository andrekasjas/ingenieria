from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  login, logout, authenticate
from Integrante.models import integrante

from Login.forms import Formulario_equipo
from .models import equipo


# Create your views here.

class registro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'Autenticacion/registro.html',{'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            usuario = form.save()
            login(request, usuario)
            return redirect('/equipos')
        else:
            return render(request, 'Autenticacion/registro.html',{'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def logear(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('/equipos')
    return render(request, 'Autenticacion/login.html',{'form':form})

def equipos(request):
    equipos = equipo.objects.filter(autor = request.user).order_by('-created')
    return render(request,'equipo/equipos.html',{'equipos':equipos})

def agregar_equipo(request):
    if (request.method == "POST"):
        formulario = Formulario_equipo(data = request.POST)
        if (formulario.is_valid()):
            nombre = formulario.cleaned_data.get('nombre')
            integrantes = formulario.cleaned_data.get('integrantess') 
            users = integrante.objects.filter(id__in=integrantes)

            try:
                add = equipo.objects.create(nombre = nombre, autor = request.user)
                add.integrante.set(users)
                add.save()
                return redirect('/equipos')
            except:
                return redirect('/contactame/?novalido')
    formulario = Formulario_equipo()
    
    return render(request, "equipo/agregar_equipo.html",{'formulario':formulario})