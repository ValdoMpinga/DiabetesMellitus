from django.shortcuts import render
from .models import predictPreview

def diagnostic(request):
    if request.method == 'POST':
        print("yo")
        predictPreview()
        return render(request,'diagnostic/diagnostic.html')
    else:
        print("Ha")
        return render(request,'diagnostic/diagnostic.html')

