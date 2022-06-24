from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, HttpResponseRedirect


def index(request):
    return render(request,'index.html')

def apoiar(request):
    return render(request,'apoiar.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def diagnostico(request):
    return render(request,'diagnostico.html')

def base(request):
    return render(request,'base.html')

def diabetes(request):
    return render(request,'diabetes.html')

def diabetesTipo1(request):
    return render(request,'diabetesTipo1.html')


