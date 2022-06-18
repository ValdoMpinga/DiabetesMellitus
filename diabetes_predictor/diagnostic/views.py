from cmath import log
from django.shortcuts import render
from .diabetes.diabetesForm import DiabetesForm
from .diabetes_predictor.diabetesPredictor import Predict
import json
from django.http import HttpResponse

def diagnostic(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        form = DiabetesForm

        prediction = Predict(jsonData)

        data = {'prediction': prediction[0],
                'probability': prediction[1]}
        data = json.dumps(data)
        context = {
            'form': form,
        }
        # print("Home:")
        # print(prediction)
        response = HttpResponse(data, content_type='application/json charset=utf-8')
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
