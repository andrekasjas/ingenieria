from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  login, logout, authenticate

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
            return redirect('/')
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
                return redirect('/')
    return render(request, 'Autenticacion/login.html',{'form':form})