from django.shortcuts import render
# from .models import predictPreview
from .diabetes.diabetesForm import DiabetesForm


def diagnostic(request):
    if request.method == 'POST':
        print("yo")
        # predictPreview()
        form = DiabetesForm
        context = {
            'form': form
        }
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
