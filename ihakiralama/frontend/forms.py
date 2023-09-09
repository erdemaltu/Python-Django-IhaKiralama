from django import forms
from django.contrib.auth.forms import UserCreationForm
from hesaplar.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'UserName or Email',
        'id':'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'id':'password'
    }))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'UserName',
        'id':'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Your Email',
        'id':'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'id':'password'
    }))

    class Meta:
        model =  CustomUser
        fields = ['username', 'email', 'password']