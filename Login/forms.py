from cProfile import label
from django import forms
from .models import integrante


class Formulario_equipo(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class':'form-control','style':'width:300%'}))
    integrantess = forms.ModelMultipleChoiceField(label="Integrantes", widget=forms.SelectMultiple(attrs={'class':'form-control','style':'width:300%'}),
                                          queryset= integrante.objects.all().order_by('-created'))