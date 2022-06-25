from cmath import log
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from forms.login.loginForm import LoginForm
from django.contrib import messages
from bll.userContribution.contribuition import contributionIntentValidator
import globalVars
from django.http import HttpResponse
from register import models as userModel

# Renders login page and and handles users authentication


def loginFunction(request):
    if request.method == "GET":
        form = LoginForm
        context = {'form': form}
        return render(request, 'login/login.html', context=context)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        context = {'form': form}
        user = authenticate(request, username=form.data['username'], password=form.data['password'])
        if user is not None:
            print("User authenticated: ", form.data['username'])
            login(request, user)

            print("Contrib day: ", request.user.contribuition_date)
            days = contributionIntentValidator(request.user.contribuition_date)
         
            if days == 1:
                globalVars.days = 0
                return redirect('/projectsupport')
            else:
                globalVars.days = days['days']
                return redirect('/userprofile')

        else:
            print("Here")
            messages.error(request, 'Nome do usuário ou palavra passe errada')
            return render(request, 'login/login.html', context)
