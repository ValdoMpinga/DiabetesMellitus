from django.shortcuts import render
from .models import predictPreview
from django.shortcuts import render

def diagnostic(request):
    if request.method == 'POST':
        print("yo")
        predictPreview()
        return render(request,'diagnostic/diagnostic.html')
    else:
        return render(request,'diagnostic/diagnostic.html')

