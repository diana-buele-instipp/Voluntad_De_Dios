from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Tu teléfono'}),
        }