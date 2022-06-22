

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

#renders index.html page
def index(request):
    return render(request,'index.html')
