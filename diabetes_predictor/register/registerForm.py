from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserModel


class CreateUserForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'please enter password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'please confirm password'}))
    class Meta:
        model = UserModel
        fields =['first_name','last_name', 'email','password1', 'password2']
