from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from register.models import UserModel

# Registation form


class CreateUserForm(ModelForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome de usuário', 'type': 'text'}))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Primeiro nome', 'type': 'text'}))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Último nome', 'type': 'text'}))

    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Palavra passe'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirmação da palavra-passe'}))

    class Meta:
        model = UserModel

        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("As palavra chaves devem ser iguais!")
        return self.cleaned_data
