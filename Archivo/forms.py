from pickle import TRUE
from django import forms
from Integrante.models import integrante


class Formulario_archivos(forms.Form):
    OPTIONS =(
        ("Sprint", "Sprint"),
        ("Sprint planing", "Sprint planing"),
        ("Sprint stand-up", "Sprint stand-up"),
        ("Sprint review", "Sprint review"),
        ("Sprint retrospective", "Sprint retrospective"),
    )

    integrantes = integrante.objects.all()
    OPTIONS_i = []
    for inte in integrantes:
        OPTIONS_i.append((inte.id, inte.nombre))
    
    tarea = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(choices = OPTIONS)
    autor = forms.ChoiceField(choices = OPTIONS_i)
    estado = forms.BooleanField(required=False, initial=False)
    url_archivo = forms.FileField(required=False)
    
