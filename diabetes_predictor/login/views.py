from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .loginForm import LoginForm
from django.contrib import messages
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
        print(form.data['email'])
        user = authenticate(request, 
                            username=form.data['email'],
                            password = form.data['password'])
        print("User ", user)
        if user is not None:
            login(request , user)
            return redirect('/projectsupport')
        else:
            messages.info(request, 'Email or password incorrect')
	
        form = LoginForm
        context = {
            'form' : form
        }
        return render(request,'login/login.html', context = context)

def logoutFunc(request):
    logout(request)
    return redirect('/login')
