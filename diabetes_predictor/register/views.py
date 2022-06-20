import logging
from django.shortcuts import render, redirect
from django.shortcuts import render
from .registerForm import CreateUserForm
from .models import UserModel


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            print(first_name, last_name, username, email)
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                raw_password = form.cleaned_data['password1']
                data = UserModel(first_name=first_name,
                                 last_name=last_name,
                                 username=username,
                                 email=email,
                                 )
                data.set_password(raw_password)
                data.save()

    context = {'form': form}
    return render(request, 'register/register.html', context)
