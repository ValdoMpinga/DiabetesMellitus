from django.shortcuts import render
from .diabetes.diabetesForm import DiabetesForm
from .diabetes_predictor.diabetesPredictor import Predict
import json


def diagnostic(request):
    if request.method == 'POST':
        jsonData= json.loads(request.body)
        form = DiabetesForm
        context = {
            'form': form
        }
        prediction = Predict(jsonData)
        print("Home:")
        print(prediction)
        return render(request, 'diagnostic/diagnostic.html', context=context)
    else:
        print("Ha")
        form = DiabetesForm(request.POST)
        form = DiabetesForm
        context = {
            'form': form
        }
        # name = {
        #     "n": "Pedro"
        # }

        # context = {
        #     "first_name": "Naveen",
        #     "last_name": "Arora",
        # }

      #  return render(request, 'diagnostic/diagnostic.html', {'x': name, 'v': context})
        return render(request, 'diagnostic/diagnostic.html', context=context)
