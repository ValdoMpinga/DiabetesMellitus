from django.test import TestCase
import os
from unittest import skip
import pandas as pd
import re

class EncoderTests(TestCase):
    
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

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
            print(index, ' -> ', value)

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
               
    @skip("8. Already tested")
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

        #Dataframe
        currentFile = pd.read_csv('../diabetes.csv')
        diabetesFrame = pd.DataFrame(diabetesDictionary)
        

        #columns
        ageColumn = currentFile['2. Qual a sua idade?']
        weightColumn = currentFile['3. Qual o seu peso?']
        heightColumn = currentFile['4. Qual a sua altura?']
        waistColumn = currentFile['5. Qual a Medida da sua cintura?']
        vegetablesColumn = currentFile['8. Com que regularidade come vegetais e/ou frutas (sopa, salada, legumes cozidos, entre outros)?']
        diabeticFamilyColumn = currentFile['9. Tem algum membro de família próximo ou outros familiares a quem foi diagnosticado diabetes (Tipo 1 ou Tipo 2)?']
        smokeColumn = currentFile['11. Você fuma?']
        highBloodGlucoseColumn = currentFile[
            '12. Alguma vez teve açúcar (glicemia) elevado no sangue (ex.: num exame de saúde, durante um período de doença ou durante a gravidez)?']
        glucoseAnalysisColumn = currentFile['13. Quanto teve de glicose na sua última análise (mg/dL)?']
        glucoseLevelChangeColumn = currentFile['14. Alguma vez teve alteração do seu nível de glicose?']
        womanGlucoseChangeColumn = currentFile['15. Se mulher, alguma vez teve alteração do seu nível de glicose, diabetes durante a gravidez ou filhos com mais de 4 quilos à nascença?']
        areYouDiabeticColumn = currentFile['16. Tem diabetes?']
        
    
        #1.Sex
        diabetesFrame['sex'] = currentFile['1. Qual o seu sexo?']
        diabetesFrame['sex'] = diabetesFrame['sex'].str.replace('Masculino', '1')
        diabetesFrame['sex'] = diabetesFrame['sex'].str.replace('Feminino', '0')

        #2.Age
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
                
                
        #4.Weight
        currentFile['3. Qual o seu peso?'] = currentFile['3. Qual o seu peso?'].str.replace(',', '.')
        currentFile['3. Qual o seu peso?'] = currentFile['3. Qual o seu peso?'].str.replace(' ', '')
        weightColumn = currentFile['3. Qual o seu peso?']

        for index, col in enumerate(weightColumn):
            value = re.sub('\D', '', col)
            diabetesFrame['weight'][index] = int(value)
            
        #5.Height
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
                
            diabetesFrame['height'][index]=value
        
        #6.waist
        for index, col in enumerate(waistColumn):
            if col == "Homens - Menos de 94 cm | Mulheres - Menos de 80 cm":
                diabetesFrame['waist1'][index] = 1
                diabetesFrame['waist2'][index] = 0
                diabetesFrame['waist3'][index] = 0
                diabetesFrame['waist4'][index] = 0
            elif col == "Homens - 94-102 cm | Mulheres - 80-88 cm":
                diabetesFrame['waist1'][index] = 0
                diabetesFrame['waist2'][index] = 1
                diabetesFrame['waist3'][index] = 0
                diabetesFrame['waist4'][index] = 0
            elif col == "Homens - Mais de 102 cm | Mulheres - Mais de 88 cm":
                diabetesFrame['waist1'][index] = 0
                diabetesFrame['waist2'][index] = 0
                diabetesFrame['waist3'][index] = 1
                diabetesFrame['waist4'][index] = 0
            elif col == "Não sei":
                diabetesFrame['waist1'][index] = 0
                diabetesFrame['waist2'][index] = 0
                diabetesFrame['waist3'][index] = 0
                diabetesFrame['waist4'][index] = 1
               
        #7.IMC
        for index, col in enumerate(heightColumn):
            value = (
                diabetesFrame['weight'][index] /
                (pow(diabetesFrame['height'][index], 2)) )/45
            if value >1:
                diabetesFrame['imc'][index] = 1
            elif value <= 1:
                diabetesFrame['imc'][index] = 0
        
        
        #8.Exercise
        diabetesFrame['physicalExercise'] = currentFile['6. Pratica, diariamente, atividade física com alum esforço durante pelo menos 30 minutos(ex.: no trabalho, tempo livre, caminhada, ... )?']
        diabetesFrame['physicalExercise'] = diabetesFrame['physicalExercise'].str.replace('Sim', '1')
        diabetesFrame['physicalExercise'] = diabetesFrame['physicalExercise'].str.replace('Não', '0')

    
        #9.Hypertension pills
        diabetesFrame['hypertensionPills'] = currentFile['7. Toma regularmente ou já tomou algum medicamento para a Hipertensão Arterial?']
        diabetesFrame['hypertensionPills'] = diabetesFrame['hypertensionPills'].str.replace('Sim', '1')
        diabetesFrame['hypertensionPills'] = diabetesFrame['hypertensionPills'].str.replace('Não', '0')

        #10.Fruits and vegetables
        for index, col in enumerate(vegetablesColumn):
            if col == "Todos os dias":
                diabetesFrame['fruitsAndVegetables1'][index] = 1
                diabetesFrame['fruitsAndVegetables2'][index] = 0
                diabetesFrame['fruitsAndVegetables3'][index] = 0
            elif col == "As vezes":
                diabetesFrame['fruitsAndVegetables1'][index] = 0
                diabetesFrame['fruitsAndVegetables2'][index] = 1
                diabetesFrame['fruitsAndVegetables3'][index] = 0
            elif col == "Não como":
                diabetesFrame['fruitsAndVegetables1'][index] = 0
                diabetesFrame['fruitsAndVegetables2'][index] = 0
                diabetesFrame['fruitsAndVegetables3'][index] = 1
                
        #11.Diabetic family
        for index, col in enumerate(diabeticFamilyColumn):
            if col == "Sim: avós, tias, tios ou primos em 1º grau (excepto pais, irmãos, irmãs ou filhos)?":
                diabetesFrame['diabeticFamily1'][index] = 1
                diabetesFrame['diabeticFamily2'][index] = 0
                diabetesFrame['diabeticFamily3'][index] = 0
                diabetesFrame['diabeticFamily4'][index] = 0
            elif col == "Sim: pais, irmãos, irmãs ou filhos":
                diabetesFrame['diabeticFamily1'][index] = 0
                diabetesFrame['diabeticFamily2'][index] = 1
                diabetesFrame['diabeticFamily3'][index] = 0
                diabetesFrame['diabeticFamily4'][index] = 0
            elif col == "Não":
                diabetesFrame['diabeticFamily1'][index] = 0
                diabetesFrame['diabeticFamily2'][index] = 0
                diabetesFrame['diabeticFamily3'][index] = 1
                diabetesFrame['diabeticFamily4'][index] = 0
            elif col == "Não sei":
                diabetesFrame['diabeticFamily1'][index] = 0
                diabetesFrame['diabeticFamily2'][index] = 0
                diabetesFrame['diabeticFamily3'][index] = 0
                diabetesFrame['diabeticFamily4'][index] = 1
        
        #12.Fats
        diabetesFrame['eataLotFats'] = currentFile['10.Consome diariamente alimentos ricos em gordura (ex.: frituras, salgados, enchidos, queijos, carnes gordas)?']
        diabetesFrame['eataLotFats'] = diabetesFrame['eataLotFats'].str.replace('Sim', '1')
        diabetesFrame['eataLotFats'] = diabetesFrame['eataLotFats'].str.replace('Não', '0')

        
        #13.Smoke
        for index, col in enumerate(smokeColumn):
            if col == "Não":
                diabetesFrame['smoke1'][index] = 1
                diabetesFrame['smoke2'][index] = 0
                diabetesFrame['smoke3'][index] = 0
                diabetesFrame['smoke4'][index] = 0
            elif col == "Fumava, mas parei":
                diabetesFrame['smoke1'][index] = 0
                diabetesFrame['smoke2'][index] = 1
                diabetesFrame['smoke3'][index] = 0
                diabetesFrame['smoke4'][index] = 0
            elif col == "Fumo 1 a 10 cigarros por dia":
                diabetesFrame['smoke1'][index] = 0
                diabetesFrame['smoke2'][index] = 0
                diabetesFrame['smoke3'][index] = 1
                diabetesFrame['smoke4'][index] = 0
            elif col == "Fumo mais de 10 cigarros por dia":
                diabetesFrame['smoke1'][index] = 0
                diabetesFrame['smoke2'][index] = 0
                diabetesFrame['smoke3'][index] = 0
                diabetesFrame['smoke4'][index] = 1
                
        #14.High blood glucose
        for index, col in enumerate(highBloodGlucoseColumn):
            if col == "Sim":
                diabetesFrame['highBloodGlucose1'][index] = 1
                diabetesFrame['highBloodGlucose2'][index] = 0
                diabetesFrame['highBloodGlucose3'][index] = 0
            elif col == "Não":
                diabetesFrame['highBloodGlucose1'][index] = 0
                diabetesFrame['highBloodGlucose2'][index] = 1
                diabetesFrame['highBloodGlucose3'][index] = 0
            elif col == "Não sei":
                diabetesFrame['highBloodGlucose1'][index] = 0
                diabetesFrame['highBloodGlucose2'][index] = 0
                diabetesFrame['highBloodGlucose3'][index] = 1
                
        #15.Glucose analysis
        for index, col in enumerate(glucoseAnalysisColumn):
            if col == "Não sei":
                diabetesFrame['glucoseAnalysis1'][index] = 1
                diabetesFrame['glucoseAnalysis2'][index] = 0
            else:
                value = re.sub('\D', '', col)
                value = int(value)
                diabetesFrame['glucoseAnalysis1'][index] = 0    
                if value/450 > 1:
                    diabetesFrame['glucoseAnalysis2'][index] = 1
                else:
                    diabetesFrame['glucoseAnalysis2'][index] = 0

        #16.Glucose level change
        for index, col in enumerate(glucoseLevelChangeColumn):
            if col == "Sim":
                diabetesFrame['glucoseLevelChange1'][index] = 1
                diabetesFrame['glucoseLevelChange2'][index] = 0
                diabetesFrame['glucoseLevelChange3'][index] = 0
            elif col == "Não":
                diabetesFrame['glucoseLevelChange1'][index] = 0
                diabetesFrame['glucoseLevelChange2'][index] = 1
                diabetesFrame['glucoseLevelChange3'][index] = 0
            elif col == "Não sei":
                diabetesFrame['glucoseLevelChange1'][index] = 0
                diabetesFrame['glucoseLevelChange2'][index] = 0
                diabetesFrame['glucoseLevelChange3'][index] = 1
                
        #17.woman Glucose Change
        for index, col in enumerate(womanGlucoseChangeColumn):
            if col == "Sim":
                diabetesFrame['womanGlucoseChange1'][index] = 1
                diabetesFrame['womanGlucoseChange2'][index] = 0
                diabetesFrame['womanGlucoseChange3'][index] = 0
                diabetesFrame['womanGlucoseChange4'][index] = 0
            elif col == "Não":
                diabetesFrame['womanGlucoseChange1'][index] = 0
                diabetesFrame['womanGlucoseChange2'][index] = 1
                diabetesFrame['womanGlucoseChange3'][index] = 0
                diabetesFrame['womanGlucoseChange4'][index] = 0
            elif col == "Não sou mulher":
                diabetesFrame['womanGlucoseChange1'][index] = 0
                diabetesFrame['womanGlucoseChange2'][index] = 0
                diabetesFrame['womanGlucoseChange3'][index] = 1
                diabetesFrame['womanGlucoseChange4'][index] = 0
            elif col == "Não sei":
                diabetesFrame['womanGlucoseChange1'][index] = 0
                diabetesFrame['womanGlucoseChange2'][index] = 0
                diabetesFrame['womanGlucoseChange3'][index] = 0
                diabetesFrame['womanGlucoseChange4'][index] = 1
        #for index,col in enumerate(ageColumn):
        
        #16.Are you diabetic
        for index, col in enumerate(areYouDiabeticColumn):
            if col == "Sim, diagnosticada pelo médico":
                diabetesFrame['areYouDiabetic'][index] = 1
            elif col == "Não, de acordo com o meu médico":
                diabetesFrame['areYouDiabetic'][index] = 0
            elif col == "Não sei":
                diabetesFrame['areYouDiabetic'][index] = 0.50

        
        print(diabetesFrame[['glucoseAnalysis1','glucoseAnalysis2']].to_string())
        diabetesFrame.drop(['weight', 'height'], axis= 1, inplace = True)
        diabetesFrame.to_csv('diabetesOutput.csv', index=False)


        
    
    




        



