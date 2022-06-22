from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse
import globalVars

#Renders user profile page and handles user logout

def user_profile(request):
    if request.method == 'POST':
        print(request.user.contribuition_date)
        logout(request)
        print(globalVars.days)
        return HttpResponse(status=204)
    elif request.method == "GET":
        context={ "days": globalVars.days}
        return render(request, 'user_profile/user_profile.html', context=context)
