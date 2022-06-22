from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
#Login form
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome do usuário', 'type': 'text'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control passwordField ', 'placeholder': 'Palavra-passe', 'type': 'password'}))
