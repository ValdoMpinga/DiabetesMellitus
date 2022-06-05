from django.shortcuts import render
from encoder import encoder
from .models import saveUserContribute
import pandas as pd

def project_support(request):
    if request.method == "POST":
        print("POST")
        userContribute = encoder.Encoder("Masculino",
        "Menos de 45 anos",
        "80kg",
        "1.70m",
        "Homens - Menos de 94 cm | Mulheres - Menos de 80 cm",
        "Sim",
        "Sim",
        "As vezes",
        "Sim: pais, irmãos, irmãs ou filhos", "Não", "Fumo 1 a 10 cigarros por dia",
        "Não", "400", "Não sei",
        "Não sou mulher",
        "Não sei")
        print("here: ",userContribute)
        saveUserContribute(userContribute)
        return render(request,'project_support/project_support.html')
    else:
        print("GET")
        return render(request,'project_support/project_support.html')


