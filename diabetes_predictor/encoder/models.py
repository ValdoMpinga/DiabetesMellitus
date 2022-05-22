from django.db import models
from helpers.encoderHelper import *
import encoder
# Create your models here.
import pandas as pd
pd.set_option('display.max_columns', None)

def encodeDiabetesFile():
    currentFile = pd.read_csv('../diabetes.csv')
    diabetesDictionary = {
        'sex': [],
        'age1': [],
        'age2': [],
        'age3': [],
        'age4': [],
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

    res = {}
    for index, row in currentFile.iterrows():
        encoderObject = encoder.Encoder(
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
        ageObject = encoderObject['age']
        waistObject = encoderObject['waist']
        fruitsObject = encoderObject['fruits']
        diabeticFamilyObject = encoderObject['diabeticFamily']
        smokeObject = encoderObject['smoke']
        highBloodGlucoseObject = encoderObject['highBloodGlucose']
        glucoseAnalysisObject = encoderObject['glucoseAnalysis']
        glucoseLevelChangeObject = encoderObject['glucoseLevelChange']
        womanGlucoseObject = encoderObject['womanGlucose']
        areYouDiabeticObject = encoderObject['areYouDiabetic']

        # Sex
        diabetesFrame.at[index, 'sex'] = encoderObject['sex']

        # Age
        diabetesFrame.at[index, 'age1'] = ageObject['age1']
        diabetesFrame.at[index, 'age2'] = ageObject['age2']
        diabetesFrame.at[index, 'age3'] = ageObject['age3']
        diabetesFrame.at[index, 'age4'] = ageObject['age4']

        # Waist
        diabetesFrame.at[index, 'waist1'] = waistObject['waist1']
        diabetesFrame.at[index, 'waist2'] = waistObject['waist2']
        diabetesFrame.at[index, 'waist3'] = waistObject['waist3']
        diabetesFrame.at[index, 'waist4'] = waistObject['waist4']

        # imc
        diabetesFrame.at[index, 'imc'] = encoderObject['imc']

        # exercise
        diabetesFrame.at[index,
                         'physicalExercise'] = encoderObject['exercise']

        # pills
        diabetesFrame.at[index,
                         'hypertensionPills'] = encoderObject['pills']

        # Fruits
        diabetesFrame.at[index,
                         'fruitsAndVegetables1'] = fruitsObject['fruit1']
        diabetesFrame.at[index,
                         'fruitsAndVegetables2'] = fruitsObject['fruit2']
        diabetesFrame.at[index,
                         'fruitsAndVegetables3'] = fruitsObject['fruit3']

        # Diabetic family
        diabetesFrame.at[index,
                         'diabeticFamily1'] = diabeticFamilyObject['diabeticFamily1']
        diabetesFrame.at[index,
                         'diabeticFamily2'] = diabeticFamilyObject['diabeticFamily2']
        diabetesFrame.at[index,
                         'diabeticFamily3'] = diabeticFamilyObject['diabeticFamily3']
        diabetesFrame.at[index,
                         'diabeticFamily4'] = diabeticFamilyObject['diabeticFamily4']

        # Fats
        diabetesFrame.at[index,
                         'eataLotFats'] = encoderObject['fats']
        
        #Smoke
        diabetesFrame.at[index,
                         'smoke1'] = smokeObject['smoke1']
        diabetesFrame.at[index,
                         'smoke2'] = smokeObject['smoke2']
        diabetesFrame.at[index,
                         'smoke3'] = smokeObject['smoke3']
        diabetesFrame.at[index,
                         'smoke4'] = smokeObject['smoke4']
        
        #High blood glucose
        diabetesFrame.at[index,
                         'highBloodGlucose1'] = highBloodGlucoseObject['glucose1']
        diabetesFrame.at[index,
                         'highBloodGlucose2'] =  highBloodGlucoseObject['glucose2']
        diabetesFrame.at[index,
                         'highBloodGlucose3'] = highBloodGlucoseObject['glucose3']
        
        #Glucose analysis
        diabetesFrame.at[index,
                         'glucoseAnalysis1'] = glucoseAnalysisObject['glucoseAnalysis1']
        diabetesFrame.at[index,
                         'glucoseAnalysis2'] = glucoseAnalysisObject['glucoseAnalysis2']
        
        #Glucose level change
        diabetesFrame.at[index,
                         'glucoseLevelChange1'] = glucoseLevelChangeObject['glucoseLevel1']
        diabetesFrame.at[index,
                         'glucoseLevelChange2'] = glucoseLevelChangeObject['glucoseLevel2']
        diabetesFrame.at[index,
                         'glucoseLevelChange3'] = glucoseLevelChangeObject['glucoseLevel3']
        
        #Woman glucose
        diabetesFrame.at[index,
                         'womanGlucoseChange1'] = womanGlucoseObject['womanGlucoseChange1']
        diabetesFrame.at[index,
                         'womanGlucoseChange2'] = womanGlucoseObject['womanGlucoseChange2']
        diabetesFrame.at[index,
                         'womanGlucoseChange3'] = womanGlucoseObject['womanGlucoseChange3']
        diabetesFrame.at[index,
                         'womanGlucoseChange4'] = womanGlucoseObject['womanGlucoseChange4']

        #Glucose level change
        diabetesFrame.at[index,
                         'areYouDiabetic'] = encoderObject['areYouDiabetic']
        
        diabetesFrame.to_csv('encodedDiabetesFile.csv', index=False)
    
    #print("here")
    #print(diabetesFrame[['womanGlucoseChange1', 'womanGlucoseChange2','womanGlucoseChange3', 'womanGlucoseChange4']])
    #print(diabetesFrame['areYouDiabetic'])
    #print(diabetesFrame)


encodeDiabetesFile()
