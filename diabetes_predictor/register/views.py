from django.shortcuts import render, redirect
from forms.register.registerForm import CreateUserForm
from .models import UserModel
from django.contrib import messages
# Renders register page and and handles users registation


def register(request):

    if request.method == "GET":
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'register/register.html', context)
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        context = {'form': form}
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
                data.set_password(raw_password)  # encrypts passwords
                data.save()
                return redirect('/login')
            else:
                messages.info(request, 'invalid registration details')
        return render(request, 'register/register.html', context)
