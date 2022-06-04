from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def diagnostic(request):
    return render(request,'diagnostic/diagnostic.html')

