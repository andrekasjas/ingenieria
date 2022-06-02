from django import forms


class Formulario_integrante(forms.Form):
    OPTIONS =(
        ("1", "Product Owner"),
        ("2", "Scrum Master"),
        ("3", "Development Team"),
    )
    nombre = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(choices = OPTIONS)