from django.shortcuts import render
from forms.diagnostic.diagnosticForm import DiabetesForm
from .diabetes_predictor_ai.diabetesPredictor import predict
import json
from django.http import HttpResponse
from diabetes_dataset_migrator.exporter import diabetesDatasetExporter
def diagnostic(request):
    if request.method == 'POST':
        #Gets request  data
        jsonData = json.loads(request.body)
        
        #makes the prediction
        prediction = predict(jsonData)

        data = {'prediction': prediction[0],
                'probability': prediction[1]}
        
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
