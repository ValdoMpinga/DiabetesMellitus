from django.db import models
from helpers.encoderHelper import *
import encoder
# Create your models here.
import pandas as pd



def encodeDiabetesFile():
    currentFile = pd.read_csv('../diabetes.csv')
    diabetesFrame = pd.DataFrame(currentFile)
    diabetesDictionary = {
        'sex': [],
        'age1': [],
        'age2': [],
        'age3': [],
        'age4': [],
        'weight': [],
        'height': [],
        'imc': [],
        'waist1': [],
        'waist2': [],
        'waist3': [],
        'waist4': [],
        'physicalExercise': [],
        'hypertensionPills': [],
        'fruitsAndVegetables1': [],
        'fruitsAndVegetables2': [],
        'fruitsAndVegetables3': [],
        'diabeticFamily1': [],
        'diabeticFamily2': [],
        'diabeticFamily3': [],
        'diabeticFamily4': [],
        'eataLotFats': [],
        'smoke1': [],
        'smoke2': [],
        'smoke3': [],
        'smoke4': [],
        'highBloodGlucose1': [],
        'highBloodGlucose2': [],
        'highBloodGlucose3': [],
        'glucoseAnalysis1': [],
        'glucoseAnalysis2': [],
        'glucoseLevelChange1': [],
        'glucoseLevelChange2': [],
        'glucoseLevelChange3': [],
        'womanGlucoseChange1': [],
        'womanGlucoseChange2': [],
        'womanGlucoseChange3': [],
        'womanGlucoseChange4': [],
        'areYouDiabetic': [],
    }
    diabetesFrame = pd.DataFrame(diabetesDictionary)

    for index, row in diabetesFrame.iterrows():  
        res = encoder.Encoder(
            row['1. Qual o seu sexo?'],
            row['2. Qual a sua idade?'],
            row['3. Qual o seu peso?'],
            row['4. Qual a sua altura?'],
            row['5. Qual a Medida da sua cintura?'],
            row['6. Pratica, diariamente, atividade física com alum esforço durante pelo menos 30 minutos(ex.: no trabalho, tempo livre, caminhada, ... )?'],
            row['7. Toma regularmente ou já tomou algum medicamento para a Hipertensão Arterial?'],
            row['8. Com que regularidade come vegetais e/ou frutas (sopa, salada, legumes cozidos, entre outros)?'],
            row['9. Tem algum membro de família próximo ou outros familiares a quem foi diagnosticado diabetes (Tipo 1 ou Tipo 2)?'],
            row['10.Consome diariamente alimentos ricos em gordura (ex.: frituras, salgados, enchidos, queijos, carnes gordas)?'],
            row['11. Você fuma?'],
            row['12. Alguma vez teve açúcar (glicemia) elevado no sangue (ex.: num exame de saúde, durante um período de doença ou durante a gravidez)?'],
            row['13. Quanto teve de glicose na sua última análise (mg/dL)?'],
            row['14. Alguma vez teve alteração do seu nível de glicose?'],
            row['15. Se mulher, alguma vez teve alteração do seu nível de glicose, diabetes durante a gravidez ou filhos com mais de 4 quilos à nascença?'],
            row['16. Tem diabetes?'])
        
        diabetesDictionary['sex'][index] = res.sex
        
        print("here")
        print(res)
        print(res.sex)
        
    print("asdasas")


encodeDiabetesFile()
