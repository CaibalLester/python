from django import forms
from .models import User
from .models import Log
from .models import Ail


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['username', 'role', 'password']



class AilForm(forms.ModelForm):
    class Meta:
        model = Ail
        fields = ['fullname', 'contact', 'email', 'sss_id', 'national_id', 'occupation', 'annual_salary']

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'sss_id': forms.TextInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'annual_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
