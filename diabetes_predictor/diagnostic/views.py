from cmath import log
from django.shortcuts import render
from .diabetes.diabetesForm import DiabetesForm
from .diabetes_predictor.diabetesPredictor import Predict
import json
from django.http import HttpResponse

from project_support.models import DiabetesSamples
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os
from django.conf import settings


from data_exporter.exporter import diabetesDatasetExporter

def diagnostic(request):
    if request.method == 'POST':
        diabetesDatasetExporter()
        jsonData = json.loads(request.body)
        form = DiabetesForm

        prediction = Predict(jsonData)

        data = {'prediction': prediction[0],
                'probability': prediction[1]}
        data = json.dumps(data)
        context = {
            'form': form,
        }

        response = HttpResponse(
            data, content_type='application/json charset=utf-8')
        return response
    else:
        form = DiabetesForm(request.POST)
        form = DiabetesForm
        context = {
            'form': form,
        }

        return render(request, 'diagnostic/diagnostic.html', context=context)

        # name = {
        #     "n": "Pedro"
        # }

        # context = {
        #     "first_name": "Naveen",
        #     "last_name": "Arora",
        # }

      #  return render(request, 'diagnostic/diagnostic.html', {'x': name, 'v': context})


""""""
