from django import forms
from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'empresa', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Tu nombre',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'tu@email.com',
                'required': True,
            }),
            'empresa': forms.TextInput(attrs={
                'placeholder': 'Tu empresa (opcional)',
            }),
            'mensaje': forms.Textarea(attrs={
                'placeholder': '¿En qué puedo ayudarte?',
                'rows': 5,
                'required': True,
            }),
        }
