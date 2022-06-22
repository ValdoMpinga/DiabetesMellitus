from django.shortcuts import render

def diabetes(request):
    return render(request,'diabetes/diabetes.html')

def diabetesOne(request):
    return render(request,'diabetes/typeOneDiabetes.html')

def diabetesTwo(request):
    return render(request,'diabetes/typeTwoDiabetes.html')

def gestationalDiabetes(request):
    return render(request, 'diabetes/gestationalDiabetes.html')
