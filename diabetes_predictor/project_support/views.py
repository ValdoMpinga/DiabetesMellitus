from .bll import contribuition
from django.shortcuts import redirect, render
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
    if request.method == "GET":
        return render(request, 'project_support/project_support.html')
    else:
        if request.user.is_authenticated:
            print('yes the user is logged-in')

            # userLastContributionDate = userModel.UserModel.objects.filter(
            #     email=request.user).values('contribuition_date')
            # userLastContributionDate = list(userLastContributionDate)
            # userLastContributionDate = userLastContributionDate[0]['contribuition_date']
            # permission = contribuition.contributionIntentValidator(
            #     userLastContributionDate)
            # print(permission)

            data = {'isAuthroized': "1"}
            data = json.dumps(data)
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            print(response)
            return response
        else:
            print('no the user is not logged-in')
            data = {'isAuthroized': "-1"}
            data = json.dumps(data)
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            return response
            # return render(request, 'project_support/project_support.html')


def contribute(request):
    if request.method == 'POST':
        userLastContributionDate = userModel.UserModel.objects.filter(
        email=request.user).values('contribuition_date')
        userLastContributionDate = list(userLastContributionDate)
        userLastContributionDate = userLastContributionDate[0]['contribuition_date']

        permission = contribuition.contributionIntentValidator(
            userLastContributionDate)
        print(permission)

        if permission == 1:
            jsonData = json.loads(request.body)
            userContribute = encoderCaller(jsonData)
            
            res = {'isAuthroized': "1"}
            res = json.dumps(res)
            response = HttpResponse(res, content_type='application/json charset=utf-8')
            currentDate = datetime.datetime.strptime(
                str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
            currentDateString = currentDate
            userModel.UserModel.objects.filter(email=request.user).update(
                contribuition_date=currentDateString)
            saveUserContribute(userContribute)
            return response
        else:
            print("Herte")
            data = {'isAuthroized': "0",
                    "daysLeft": permission['days']}
            data = json.dumps(data)
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            return response
    


        """email=request.user).values('contribuition_date')
       if(userLastContribution)
        userModel.UserModel.objects.filter(
                email=request.user).update(contribuition_date=today)
        print(user.values('contribuition_date'))
        userModel.UserModel.save(update_fields[''])
        a = userModel.UserModel.objects.filter(
            email=request.user).values('contribuition_date')
        a = list(a)
        print(a[0]['contribuition_date'])

        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        print(type(d1))
        print(request.user)
        saveUserContribute(userContribute)"""
    else:
        print("Here2")
        form = ContributionForm(request.POST)
        form = ContributionForm
        context = {
            'form': form,
        }
        return render(request, 'project_support/contribute.html', context)


def encoderCaller(jsonData):
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
     return userContribute
    
