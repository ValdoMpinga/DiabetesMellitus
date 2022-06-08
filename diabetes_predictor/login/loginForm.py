from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
 

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'password'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control passwordField ', 'placeholder': 'Palavra-passe', 'type': 'password'}))
