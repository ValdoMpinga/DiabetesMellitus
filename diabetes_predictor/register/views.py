from django.shortcuts import render
from django.shortcuts import render
from .models import createUser
def register(request):
    if request.method == "POST":
        print(request.POST['firstName'])
        createUser(request.POST['firstName'])
    
    return render(request,'register/register.html')

