from django.db.models.signals import (post_save)
from bll.ai_trainer.diabetesModel import diabetesModelTrainer
from django.dispatch import receiver
from project_support.models import DiabetesSamples
from bll.userContribution.contribuition import contributionIntentValidator
from django.shortcuts import render
from bll.encoder import encoder
from .models import saveUserContribute
from .models import DiabetesSamples
from register import models as userModel
from forms.project_support.contributionForm import ContributionForm
import json
from django.http import HttpResponse
from datetime import date
import datetime
today = date.today()

# Renders project support page and checks if can or not contribute


def project_support(request):
    if request.method == "GET":
        return render(request, 'project_support/project_support.html')
    elif request.method == "POST":
        if request.user.is_authenticated:
            print('yes the user is logged-in')
            data = {'isAuthroized': "1"}
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
        userLastContributionDate = userModel.UserModel.objects.filter(
            username=request.user).values('contribuition_date')  # Gets user last contribution date
        userLastContributionDate = list(userLastContributionDate)
        print(userLastContributionDate)
        userLastContributionDate = userLastContributionDate[0]['contribuition_date']

        # Validates if user can or not contribute
        permission = contributionIntentValidator(userLastContributionDate)
        print(permission)

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
            userModel.UserModel.objects.filter(username=request.user).update(
                contribuition_date=currentDateString)  # Updates user contribute date
            saveUserContribute(userContribute)  # saves user contribute
            return response
        else:
            data = {'isAuthroized': "0", "daysLeft": permission['days']}
            data = json.dumps(data)  # convertes the response to string
            response = HttpResponse(
                data, content_type='application/json charset=utf-8')
            return response

    elif request.method == "GET":
        form = ContributionForm
        context = {
            'form': form,
        }
        return render(request, 'project_support/contribute.html', context)

# Encodes user contribute


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
@receiver(post_save, sender=DiabetesSamples)
def diagnosticInsertedHandler(sender, instance, created, *args, **kwargs):
    print(args, kwargs)
    if created:
        currentNumberOfSamples = DiabetesSamples.objects.all().count()
        if(currentNumberOfSamples % 500 == 0):
            diabetesModelTrainer(DiabetesSamples.objects.all().values_list())
    else:
        pass
