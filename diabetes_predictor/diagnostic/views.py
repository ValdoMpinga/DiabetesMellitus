from django.shortcuts import render
from .models import predictPreview


def diagnostic(request):
    if request.method == 'POST':
        print("yo")
        predictPreview()
        return render(request, 'diagnostic/diagnostic.html')
    else:
        print("Ha")
        name = {
            "n": "Pedro"
        }

        context = {
            "first_name": "Naveen",
            "last_name": "Arora",
        }

      #  return render(request, 'diagnostic/diagnostic.html', {'x': name, 'v': context})
        return render(request, 'diagnostic/diagnostic.html', [context,name])
