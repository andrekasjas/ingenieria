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
    YES_NO = ((True,"Finalizado"),(False,"En curso"))

    tarea = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(choices = OPTIONS, widget = forms.Select(attrs={'class': 'form-control',}))
    autor = forms.ModelChoiceField(queryset=integrante.objects.all().order_by("-created"), widget = forms.Select(attrs={'class': 'form-control'}))
    estado = forms.BooleanField(required=False, initial=False, widget=forms.RadioSelect(choices=YES_NO))
    url_archivo = forms.FileField(label="Archivo", required=False)
    
