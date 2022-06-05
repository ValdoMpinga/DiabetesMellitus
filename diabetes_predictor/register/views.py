from django.shortcuts import render,redirect
from django.shortcuts import render
from .registerForm import CreateUserRegistationForm

def register(request):            
        form = CreateUserRegistationForm()
        context = {'form' : form}
        if request.method == 'POST':
            form = CreateUserRegistationForm(request.POST)
            if form.is_valid():
                print("valid")
                form.save()
                #redirect('login')
            else:
                print("Error saving user")
        
        return render(request,'register/register.html', context)



