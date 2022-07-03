from django.shortcuts import render
from forms.diagnostic.diagnosticForm import DiabetesForm
from .diabetes_predictor_ai.diabetesPredictor import predict
import json
from django.http import HttpResponse
from diabetes_dataset_migrator.exporter import diabetesDatasetExporter
from django.conf import settings
from .models import Diagnostic
from datetime import datetime

def diagnostic(request):
    if request.method == 'POST':
        #Gets request  data
        jsonData = json.loads(request.body)
        # diabetesDatasetExporter()
        #makes the prediction
        prediction = predict(jsonData)

        data = {'prediction': prediction[0],
                'probability': prediction[1]}
        probability =(prediction[1] * 100)
        diagnosticInstance = Diagnostic(diagnosticResult=prediction[0],
                                        diagnosticProbability=int(probability),
                                        diagnosticDate=datetime.now())
        diagnosticInstance.save()
        
        #converts json data to string
        data = json.dumps(data)
  
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
