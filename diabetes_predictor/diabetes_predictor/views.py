from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, HttpResponseRedirect

def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')


