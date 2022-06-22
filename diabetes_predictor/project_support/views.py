from project_support.models import DiabetesSamples
import re
from .bll import contribuition
from django.shortcuts import  render
from encoder import encoder
from .models import saveUserContribute
from .models import DiabetesSamples
from register import models as userModel
from .contributionForm import ContributionForm
import json
from django.http import HttpResponse
from datetime import date
import datetime
today = date.today()
from django.dispatch import receiver
from django.db.models.signals import ( post_save)
from ai_trainer.diabetes_model.diabetesModel import diabetesModelTrainer

def project_support(request):
    if request.method == "GET":
        return render(request, 'project_support/project_support.html')
    else:
        if request.user.is_authenticated:
            print('yes the user is logged-in')
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
            username=request.user).values('contribuition_date')
        userLastContributionDate = list(userLastContributionDate)
        print(userLastContributionDate)
        userLastContributionDate = userLastContributionDate[0]['contribuition_date']

        permission = contribuition.contributionIntentValidator(
            userLastContributionDate)
        print(permission)

        if permission == 1:
            jsonData = json.loads(request.body)
            userContribute = encoderCaller(jsonData)

            res = {'isAuthroized': "1"}
            res = json.dumps(res)
            response = HttpResponse(
                res, content_type='application/json charset=utf-8')
            currentDate = datetime.datetime.strptime(
                str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
            currentDateString = currentDate
            userModel.UserModel.objects.filter(username=request.user).update(contribuition_date=currentDateString)
            saveUserContribute(userContribute)
            return response
        else:
            data = {'isAuthroized': "0",
                    "daysLeft": permission['days']}
            data = json.dumps(data)
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            return response

    else:
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


@receiver(post_save, sender=DiabetesSamples)

def diagnosticInsertedHandler(sender, instance, created, *args, **kwargs):
    print(args,kwargs)
    if created:
        currentNumberOfSamples = DiabetesSamples.objects.all().count()
        if(currentNumberOfSamples % 500 == 0):
            diabetesModelTrainer(DiabetesSamples.objects.all().values_list())
       
        
    else:
        print("Not mailing him!")

