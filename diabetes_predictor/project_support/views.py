from django.shortcuts import render
from encoder import encoder
from .models import saveUserContribute
from register import models as userModel
import pandas as pd
from django.contrib.auth import authenticate, login, logout, user_logged_in
from .contributionForm import ContributionForm
import json
from django.http import HttpResponse
from datetime import date
import datetime
today = date.today()


def project_support(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            print('yes the user is logged-in')
        else:
            print('no the user is not logged-in')
        return render(request, 'project_support/project_support.html')
    else:
        print("GET")
        return render(request, 'project_support/project_support.html')


def contribute(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        userContribute = encoder.Encoder(1,
                                         jsonData['sex'],
                                         jsonData['age'],
                                         jsonData['weight'],
                                         jsonData['height'],
                                         jsonData['waist'],
                                         jsonData['exercise'],
                                         jsonData['pills'],
                                         jsonData['fruits'],
                                         jsonData['diabeticFamily'],
                                         jsonData['fats'],
                                         jsonData['smoke'],
                                         jsonData['highBloodGlucose'],
                                         jsonData['glucoseAnalysis'],
                                         jsonData['glucoseLevelChange'],
                                         jsonData['womanGlucose'],
                                         jsonData['areYouDiabetic'],)

        # user = userModel.UserModel.objects.get(email=request.user)
       # user.save(contribuition_date=[today])
        userLastContributionDate = userModel.UserModel.objects.filter(email=request.user).values('contribuition_date')
        userLastContributionDate = list(userLastContributionDate)
        userLastContributionDate = userLastContributionDate[0]['contribuition_date']
      
        if(userLastContributionDate == None):
            print("None goes jere")
        else:
            # #print("Date existense goes here")
            # print(datetime.datetime.strptime(
            #     str(today), '%Y-%m-%d').strftime('%d/%m/%Y'))
            # print(userLastContributionDate)
            currentDate = datetime.datetime.strptime(str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
            currentDateString = currentDate
            currentDate = datetime.datetime.strptime(currentDate, "%d/%m/%Y")
            lastContribuitionDate = datetime.datetime.strptime(
                userLastContributionDate,"%d/%m/%Y")
            
            daysOfDifference = (currentDate - lastContribuitionDate).days
            print(daysOfDifference)
            if daysOfDifference >= 365:
                userModel.UserModel.objects.filter(
                    email=request.user).update(contribuition_date=currentDateString)
                saveUserContribute(userContribute)
                print("contributed!")
            else:
                print("Early to contribute!")

        #     email=request.user).values('contribuition_date')
    #    if(userLastContribution)
    #     userModel.UserModel.objects.filter(
    #             email=request.user).update(contribuition_date=today)
        # print(user.values('contribuition_date'))
        # userModel.UserModel.save(update_fields[''])
        # a = userModel.UserModel.objects.filter(
        #     email=request.user).values('contribuition_date')
        # a = list(a)
        # print(a[0]['contribuition_date'])

        # # dd/mm/YY
        # d1 = today.strftime("%d/%m/%Y")
        # print(type(d1))
        # print(request.user)


        # saveUserContribute(userContribute)

        response = HttpResponse(
            jsonData['sex'], content_type='application/json charset=utf-8')
        return response
    else:
        print("Here2")
        form = ContributionForm(request.POST)
        form = ContributionForm
        context = {
            'form': form,
        }
        return render(request, 'project_support/contribute.html', context)
