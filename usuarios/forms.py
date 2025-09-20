from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from planos.models import Plano

class UsuarioCadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    plano = forms.ModelChoiceField(
        queryset=Plano.objects.all(),
        required=False,
        empty_label="Selecione um plano"
    )

    class Meta:
        model = Usuario
        fields = ("username", "email", "plano", "password1", "password2")
