from django import forms


class Formulario_integrante(forms.Form):
    OPTIONS =(
        ("Product Owner", "Product Owner"),
        ("Scrum Master", "Scrum Master"),
        ("Development Team", "Development Team"),
    )
    nombre = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(choices = OPTIONS, widget=forms.Select(attrs={'class': 'form-control'}))