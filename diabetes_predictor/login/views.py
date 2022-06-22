from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from forms.login.loginForm import LoginForm
from django.contrib import messages
from bll.userContribution import daysCalculator
import globalVars

# Renders login page and and handles users authentication

def loginFunction(request):
    if request.method == "GET":
        form = LoginForm
        context = {'form': form}
        return render(request, 'login/login.html', context=context)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(request, username=form.data['username'],password=form.data['password'])
        if user is not None:
            print("User authenticated: ", form.data['username'])
            login(request, user)
            print("User last contribution date: ",
                  request.user.contribuition_date)
            days = daysCalculator.daysCalculator( request.user.contribuition_date)
            globalVars.days = days
            return redirect('/projectsupport')
        else:
            messages.info(request, 'Username or password incorrect')
