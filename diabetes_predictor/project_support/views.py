from distutils.log import log
import globalVars
from django.db.models.signals import (post_save)
from bll.ai_trainer.re_trainer_scheduler import trainerScheculer
from django.dispatch import receiver
from ai_trainer_condition.models import AI_TrainerCondition
from bll.userContribution.contribuition import contributionIntentValidator
from django.shortcuts import render, redirect
from bll.encoder import encoder
from bll.userContribution import saveUserContribute
from .models import DiabetesSamples
from register import models as userModel
from forms.project_support.contributionForm import ContributionForm
import json
from django.http import HttpResponse
from datetime import date
import datetime
from django.contrib.auth import logout
today = date.today()

# Renders project support page and checks if can or not contribute


def project_support(request):
    if request.method == "GET":
        return render(request, 'project_support/project_support.html')
    elif request.method == "POST":
        print(globalVars.days)
        if request.user.is_authenticated:
            print('yes the user is logged-in')
            if globalVars.days == 0:      
                data = {'isAuthroized': "1"}
                data = json.dumps(data)  # Converts data to string
                response = HttpResponse(
                    data, content_type='application/json charset=utf-8')
                return response
            else:
                data = {'isAuthroized': "0",
                        'daysLeft': globalVars.days}
                data = json.dumps(data)  # Converts data to string
                response = HttpResponse(
                    data, content_type='application/json charset=utf-8')
                return response
        
        else:
            print('no the user is not logged-in')
            data = {'isAuthroized': "-1"}
            data = json.dumps(data)  # Converts data to string
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            return response

# Renders contribution page and saves contribute if is valid


def contribute(request):
    if request.method == 'POST':
        userLastContributionDate = userModel.UserModel.objects.filter(username=request.user).values('contribuition_date')  # Gets user last contribution date
        userLastContributionDate = list(userLastContributionDate)
        print(userLastContributionDate)
        userLastContributionDate = userLastContributionDate[0]['contribuition_date']

        # Validates if user can or not contribute
        permission = contributionIntentValidator(userLastContributionDate)
        print("Perm: ",permission)

        if permission == 1:  # If user is allowed to contribute
            jsonData = json.loads(request.body)
            userContribute = encoderCaller(jsonData)  # Encodes the input data

            res = {'isAuthroized': "1"}
            res = json.dumps(res)  # convertes the response to string
            response = HttpResponse(
                res, content_type='application/json charset=utf-8')
            currentDate = datetime.datetime.strptime(
                str(today), '%Y-%m-%d').strftime('%d/%m/%Y')
            currentDateString = currentDate
            userModel.UserModel.objects.filter(username=request.user).update(contribuition_date=currentDateString)  # Updates user contribute date
            saveUserContribute.saveUserContribute(userContribute)  # saves user contribute
            globalVars.days = 366
            return response
        else:
            data = {'isAuthroized': "0", "daysLeft": permission['days']}
            data = json.dumps(data)  # convertes the response to string
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            
            return response

    elif request.method == "GET":
        if globalVars.days > 0 or request.user.is_anonymous:#forbids the access to the contribute page if the user is not logged or if he's on contribution cooldown(366 days)
            return redirect('/projectsupport/404')
        else: 
            form = ContributionForm
            context = {'form': form,}
            return render(request, 'project_support/contribute.html', context)

# Encodes user contribute

def page404(request):
    if request.method == "GET":
        return render(request, 'project_support/page404.html')


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

    
# Signal,(django trigger equivalent) that handles AI model re training after reaching a number divible by 500 on the database
# The number of re-training can be changed by the admin on the system, if on the system is not defined, by default it will be
# After 500 insertions
@receiver(post_save, sender=DiabetesSamples)
def sampleInsertedHandler(sender, instance, created, *args, **kwargs):
    print(args, kwargs)
    if created:
        currentNumberOfSamples = DiabetesSamples.objects.all().count()
        retrainerCondition = AI_TrainerCondition.objects.filter()[:1].values('re_trainNumber')
        if(not(retrainerCondition)):
            retrainerCondition = 500
        else:
            print("Not Null section")
            print(retrainerCondition)
            retrainerCondition = list(retrainerCondition)
            retrainerCondition = retrainerCondition[0]['re_trainNumber']        
        if(currentNumberOfSamples % retrainerCondition == 0):
            trainerScheculer()
    else:
        pass
