from django import forms
from .models import integrante


class Formulario_equipo(forms.Form):
    integrantes = integrante.objects.all().values()
    OPTIONS = []
    for inte in integrantes:
        OPTIONS.append((inte['id'], inte['nombre']))
    nombre = forms.CharField( max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    integrantess = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
