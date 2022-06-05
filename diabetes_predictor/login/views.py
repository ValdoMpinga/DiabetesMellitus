from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# from .loginForm import UserloginRegistationForm

def login(request):            
        # form = UserloginRegistationForm()
        # context = {'form' : form}
        # if request.method == 'POST':
        #     form = UserloginRegistationForm(request.POST)
        #     if form.is_valid():
        #         form.save()
        #     else:
        #         print("Error saving user")   
        return render(request,'register/register.html')

