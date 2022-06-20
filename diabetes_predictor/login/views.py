from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .loginForm import LoginForm
from django.contrib import messages
from .bll import daysCalculator
import globalVars
# from .loginForm import UserloginRegistationForm


def loginFunc(request):
    if request.method == "GET":
        print("hahaha")
        form = LoginForm
        context = {
            'form': form
        }
        return render(request, 'login/login.html', context=context)
    else:
        form = LoginForm(request.POST)
        print(form.data['username'])
        user = authenticate(request, 
                            username=form.data['username'],
                            password = form.data['password'])
        print("User ", user)
        if user is not None:
            login(request , user)
            print(request.user.contribuition_date)
            days = daysCalculator.daysCalculator(
                request.user.contribuition_date)
            print(days)
            globalVars.days = days 
            print(globalVars.days)
            return redirect('/projectsupport')
        
        else:
            messages.info(request, 'Username or password incorrect')
	
        form = LoginForm
        context = {
            'form' : form
        }
        return render(request,'login/login.html', context = context)
