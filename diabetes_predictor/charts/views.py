from django.shortcuts import render

# Create your views here.
def charts(request):
    return render(request, 'charts/charts.html')
