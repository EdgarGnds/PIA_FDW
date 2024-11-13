from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'email', 'contraseña', 'comentario', 'torneo' ]
        widgets = {
            'contraseña': forms.PasswordInput(), 
        }