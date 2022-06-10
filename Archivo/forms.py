from django import forms
from Integrante.models import integrante
from Login.models import equipo

OPTIONS_TIPO =(
            ("Sprint", "Sprint"),
            ("Sprint planing", "Sprint planing"),
            ("Sprint stand-up", "Sprint stand-up"),
            ("Sprint review", "Sprint review"),
            ("Sprint retrospective", "Sprint retrospective"),
        )
OPTIONS_ESTADO =(
            ("Pendiente", "Pendiente"),
            ("Ejecutandose", "Ejecutandose"),
            ("Finalizado", "Finalizado"),
        )

def formulario_equipo(equipo_id):
    class Formulario_archivos(forms.Form):
        equipos = equipo.objects.filter(id = equipo_id)
        integrante = equipos[0].integrante.all()
        tarea = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
        tipo = forms.ChoiceField(choices = OPTIONS_TIPO, widget = forms.Select(attrs={'class': 'form-control'}))
        autor = forms.ModelChoiceField(queryset=integrante.order_by("-created"), widget = forms.Select(attrs={'class': 'form-control'}))
        estado =  forms.ChoiceField(choices = OPTIONS_ESTADO, widget = forms.Select(attrs={'class': 'form-control'}))
        url_archivo = forms.FileField(label="Archivo", required=False,widget = forms.FileInput(attrs={'class': 'form-control'}))
    return Formulario_archivos

class Formulario_archivos(forms.Form):
        tarea = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control',}))
        tipo = forms.ChoiceField(choices = OPTIONS_TIPO, widget = forms.Select(attrs={'class': 'form-control'}))
        autor = forms.ModelChoiceField(queryset=integrante.objects.all().order_by("-created"), widget = forms.Select(attrs={'class': 'form-control'}))
        estado = forms.ChoiceField(choices = OPTIONS_ESTADO, widget = forms.Select(attrs={'class': 'form-control'}))
        url_archivo = forms.FileField(label="Archivo", required=False,widget = forms.Select(attrs={'class': 'form-control',}))
    
 