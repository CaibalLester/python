from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

