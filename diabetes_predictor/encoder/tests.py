from django.test import TestCase
import os
from unittest import skip
import pandas as pd
from enum import Enum
import re 

class EncoderTests(TestCase):
    
    @skip("Already tested")
    def test_readfile(self):
        file = open("../diabetes.csv","r") 
        self.assertEqual(file.readable() , True)

    #Useful for creating a new dataframa with specific fields
    @skip("1. Already tested")
    def test_pandaFrameCreator(self):
        my_dict = {
            'name': ["a", "b", "c", "d", "e", "f", "g"],
            'age': [20, 27, 35, 55, 18, 21, 35],
            'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
            
        df = pd.DataFrame(my_dict)
        
        print(df)
      
    @skip("2. Already tested")
    def test_pandaFrameDelete(self):
        my_dict = {
            'name': ["a", "b", "c", "d", "e", "f", "g"],
            'age': [20, 27, 35, 55, 18, 21, 35],
            'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
            
        df = pd.DataFrame(my_dict)
        df.drop('name',axis=1, inplace=True)
        print(df)
        
    @skip("3. Already tested")    
    def test_pandaFrameMathOperations(self):
         my_dict = {
            'age': [20, 27, 35, 55, 18, 21, 35],
            'numbers': [2, 4, 5, 6, 32, 34, 80]}
         
         df = pd.DataFrame(my_dict)
         
         df['numbers'] = df['numbers']  * 3
         print(df)
        
    @skip("4. Already tested")
    def test_columnTransference(self):
        file = pd.read_csv('../diabetes.csv')
        sexColumn = file['1. Qual o seu sexo?']
        my_dict = {
            'sex': sexColumn
        }

        print(pd.DataFrame(my_dict))
         
    @skip("5. Already tested")
    def test_columnTransformation(self):
        file = pd.read_csv('../diabetes.csv')
        sexColumn = file['1. Qual o seu sexo?']
        my_dict = {
            'sex': sexColumn
        }

        newFrame = pd.DataFrame(my_dict)
        newFrame['sex'] = newFrame['sex'].str.replace('Masculino', '1')
        newFrame['sex'] = newFrame['sex'].str.replace('Feminino','0')
        
        print(newFrame)
        
    @skip("6. Already tested")
    def test_weightHandler(self):
        currentFile = pd.read_csv('../diabetes.csv')
        
        currentFile['3. Qual o seu peso?'] =  currentFile['3. Qual o seu peso?'].str.replace(',','.')
        currentFile['3. Qual o seu peso?'] =  currentFile['3. Qual o seu peso?'].str.replace(' ','')
        weightColumn = currentFile['3. Qual o seu peso?']
        
        for index,col in enumerate(weightColumn):
            value = re.sub('\D','',col)
            print(value)

    @skip("7. Already tested")
    def test_heightHandler(self):
        currentFile = pd.read_csv('../diabetes.csv')
        currentFile['4. Qual a sua altura?'] =  currentFile['4. Qual a sua altura?'].str.replace(',','.')
        currentFile['4. Qual a sua altura?'] =  currentFile['4. Qual a sua altura?'].str.replace(' ','')
        heightColumn = currentFile['4. Qual a sua altura?']
        
        for index, col in enumerate(heightColumn):
            value = re.sub('\D','',col)
            value = int(value)/100
            
            if value < 1:
                value += 1
            elif value >= 10:
                value /= 10
                
            print(index,"->", format(value))
               
    #@skip("8. Already tested")
    def test_csvFileEncoderPreview(self):
        diabetesDictionary = {
            'sex' : [],
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
            'eataLotFats': [],
            'smoke1': [],
            'smoke2': [],
            'smoke3': [],
            'smoke4': [],
            'highBloodGlucose1': [],
            'highBloodGlucose2': [],
            'highBloodGlucose3': [],
            'glucoseAnalysis': [],
            'glucoseLevelChange1': [],
            'glucoseLevelChange2': [],
            'glucoseLevelChange3': [],
            'womanGlucoseChange1': [],
            'womanGlucoseChange2': [],
            'womanGlucoseChange3': [],
            'womanGlucoseChange4': [],
            'areYouDiabetic': []
        }

        #Dataframe
        currentFile = pd.read_csv('../diabetes.csv')
        diabetesFrame = pd.DataFrame(diabetesDictionary)
        

        #columns
        ageColumn = currentFile['2. Qual a sua idade?']
        weightColumn = currentFile['3. Qual o seu peso?']
        heightColumn = currentFile['4. Qual a sua altura?']
        weistColumn = currentFile['5. Qual a Medida da sua cintura?']
        vegetablesColumn = currentFile['8. Com que regularidade come vegetais e/ou frutas (sopa, salada, legumes cozidos, entre outros)?']
        diabeticFamilyColumn = currentFile['9. Tem algum membro de família próximo ou outros familiares a quem foi diagnosticado diabetes (Tipo 1 ou Tipo 2)?']
        smokeColumn = currentFile['11. Você fuma?']
        highBloodGlucoseColumn = currentFile[
            '12. Alguma vez teve açúcar (glicemia) elevado no sangue (ex.: num exame de saúde, durante um período de doença ou durante a gravidez)?']
        glucoseAnalysisColumn = currentFile['13. Quanto teve de glicose na sua última análise (mg/dL)?']
        glucoseLevelChangeColumn = currentFile['14. Alguma vez teve alteração do seu nível de glicose?']
        womanGlucoseChangeColumn = currentFile['15. Se mulher, alguma vez teve alteração do seu nível de glicose, diabetes durante a gravidez ou filhos com mais de 4 quilos à nascença?']
        areYouDiabeticColumn = currentFile['16. Tem diabetes?']
        
    
        #Sex
        diabetesFrame['sex'] = currentFile['1. Qual o seu sexo?']
        diabetesFrame['sex'] = diabetesFrame['sex'].str.replace('Masculino', '1')
        diabetesFrame['sex'] = diabetesFrame['sex'].str.replace('Feminino', '0')

        #Exercise
        diabetesFrame['physicalExercise'] = currentFile['6. Pratica, diariamente, atividade física com alum esforço durante pelo menos 30 minutos(ex.: no trabalho, tempo livre, caminhada, ... )?']
        diabetesFrame['physicalExercise'] = diabetesFrame['physicalExercise'].str.replace('Sim', '1')
        diabetesFrame['physicalExercise'] = diabetesFrame['physicalExercise'].str.replace('Não', '0')

        #Hypertension pills
        diabetesFrame['hypertensionPills'] = currentFile['7. Toma regularmente ou já tomou algum medicamento para a Hipertensão Arterial?']
        diabetesFrame['hypertensionPills'] = diabetesFrame['hypertensionPills'].str.replace('Sim', '1')
        diabetesFrame['hypertensionPills'] = diabetesFrame['hypertensionPills'].str.replace('Não', '0')

        #Fats
        diabetesFrame['eataLotFats'] = currentFile['10.Consome diariamente alimentos ricos em gordura (ex.: frituras, salgados, enchidos, queijos, carnes gordas)?']
        diabetesFrame['eataLotFats'] = diabetesFrame['eataLotFats'].str.replace('Sim', '1')
        diabetesFrame['eataLotFats'] = diabetesFrame['eataLotFats'].str.replace('Não', '0')

        #Fats
        diabetesFrame['eataLotFats'] = currentFile['10.Consome diariamente alimentos ricos em gordura (ex.: frituras, salgados, enchidos, queijos, carnes gordas)?']
        diabetesFrame['eataLotFats'] = diabetesFrame['eataLotFats'].str.replace('Sim', '1')
        diabetesFrame['eataLotFats'] = diabetesFrame['eataLotFats'].str.replace('Não', '0')
        
        pd.options.mode.chained_assignment = None  # default='warn'
        for index,col in enumerate(ageColumn):
            if col == "Menos de 45 anos":
                diabetesFrame['age1'][index]=1
                diabetesFrame['age2'][index]=0
                diabetesFrame['age3'][index]=0
                diabetesFrame['age4'][index]=0
            elif col =="45-54 anos":
                diabetesFrame['age1'][index]=0
                diabetesFrame['age2'][index]=1
                diabetesFrame['age3'][index]=0
                diabetesFrame['age4'][index]=0
            elif col == "55-64 anos":
                diabetesFrame['age1'][index]=0
                diabetesFrame['age2'][index]=0
                diabetesFrame['age3'][index]=1
                diabetesFrame['age4'][index]=0
            elif col =="Mais de 64 anos":
                diabetesFrame['age1'][index]=0
                diabetesFrame['age2'][index]=0
                diabetesFrame['age3'][index]=0
                diabetesFrame['age4'][index]=1
                
        #for index,col in enumerate(ageColumn):
        
        
        
        #print(diabetesFrame['eataLotFats'])
        #print(diabetesFrame[['age1','age2','age3']])
        
        

    




        



