import logging
from django.shortcuts import render, redirect
from django.shortcuts import render
from .registerForm import CreateUserForm


def register(request):
    try:
        form = CreateUserForm()

    
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                
        context = {'form': form}
        return render(request, 'register/register.html', context)
    except BaseException:
        print("-------------------------------")
        logging.exception("*Error goes here*")
     