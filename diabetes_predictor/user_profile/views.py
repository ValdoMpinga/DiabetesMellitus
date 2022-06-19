from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse
import globalVars
def user_profile(request):
    if request.method == 'POST':
        print("bellow")
        print(request.user.contribuition_date)
        logout(request)
        print(globalVars.days)
        return HttpResponse(status=204)
    else:
        context={
            "days": globalVars.days
        }
        print(globalVars.days)
        return render(request, 'user_profile/user_profile.html', context=context)
