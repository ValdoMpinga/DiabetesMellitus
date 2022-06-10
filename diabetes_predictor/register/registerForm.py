from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserModel


class CreateUserForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Primeiro nome', 'type': 'text'}))
    
    last_name = forms.CharField(widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Último nome', 'type': 'text'}))
    
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Palavra passe'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmação da palavra-passe'}))
    class Meta:
        model = UserModel
        fields =['first_name','last_name', 'email','password1', 'password2']
