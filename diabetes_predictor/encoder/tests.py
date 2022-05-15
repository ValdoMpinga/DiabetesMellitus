from django.test import TestCase
import os
from unittest import skip
import pandas as pd

class EncoderTests(TestCase):
    
    @skip("Already tested")
    def test_readfile(self):
        file = open("../diabetes.csv","r") 
        self.assertEqual(file.readable() , True)

    #Useful for creating a new dataframa with specific fields
    @skip("Already tested")
    def test_pandaFrameCreator(self):
        my_dict = {
            'name': ["a", "b", "c", "d", "e", "f", "g"],
            'age': [20, 27, 35, 55, 18, 21, 35],
            'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
            
        df = pd.DataFrame(my_dict)
        
        print(df)
      
    @skip("Already tested")
    def test_pandaFrameDelete(self):
        my_dict = {
            'name': ["a", "b", "c", "d", "e", "f", "g"],
            'age': [20, 27, 35, 55, 18, 21, 35],
            'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
            
        df = pd.DataFrame(my_dict)
        df.drop('name',axis=1, inplace=True)
        print(df)
        
    @skip("Already tested")    
    def test_pandaFrameMathOperations(self):
         my_dict = {
            'age': [20, 27, 35, 55, 18, 21, 35],
            'numbers': [2, 4, 5, 6, 32, 34, 80]}
         
         df = pd.DataFrame(my_dict)
         
         df['numbers'] = df['numbers']  * 3
         print(df)
        
    @skip("Already tested")
    def test_columnTransference(self):
        file = pd.read_csv('../diabetes.csv')
        sexColumn = file['1. Qual o seu sexo?']
        my_dict = {
            'sex': sexColumn
        }

        print(pd.DataFrame(my_dict))
         
    @skip("Already tested")
    def test_columnTransformatiion(self):
        file = pd.read_csv('../diabetes.csv')
        sexColumn = file['1. Qual o seu sexo?']
        my_dict = {
            'sex': sexColumn
        }

        newFrame = pd.DataFrame(my_dict)
        newFrame['sex'] = newFrame['sex'].str.replace('Masculino', '1')
        newFrame['sex'] = newFrame['sex'].str.replace('Feminino','0')
        
        print(newFrame)
       
  #  @skip("Already tested")
    def test_csvFileEncoderPreview(self):
        diabetesDictionary = {
            'sex' : [],
            'age1': [],
            'age2': [],
            'age3': [],
            'icm1': [],
            'imc2': [],
            'imc3': [],
            'waist1': [],
            'waist2': [],
            'waist3': [],
            'physicalExercise': [],
            'hypertensionPills': [],
            'fruitsAndVegetables1': [],
            'fruitsAndVegetables2': [],
            'diabeticFamily1': [],
            'diabeticFamily2': [],
            'diabeticFamily3': [],
            'eataLotFats': [],
            'smoke1': [],
            'smoke2': [],
            'smoke3': [],
            'highBloodGlucose1': [],
            'highBloodGlucose2': [],
            'glucoseAnalysis1': [],
            'glucoseAnalysis2': [],
            'glucoseLevelChange1': [],
            'glucoseLevelChange2': [],
            'womanGlucoseChange1': [],
            'womanGlucoseChange2': [],
            'womanGlucoseChange3': [],
            'areYouDiabetic': []
        }

        #Dataframe
        currentFile = pd.read_csv('../diabetes.csv')
        diabetesFrame = pd.DataFrame(diabetesDictionary)
        
        diabetesFrame['sex'] = currentFile['1. Qual o seu sexo?']
        diabetesFrame['sex'] = diabetesFrame['sex'].str.replace('Masculino', '1')
        diabetesFrame['sex'] = diabetesFrame['sex'].str.replace('Feminino', '0')
        
        for row in diabetesFrame.iterrows():
             diabetesFrame['age1'] = 2

        print(diabetesFrame)
        


        
