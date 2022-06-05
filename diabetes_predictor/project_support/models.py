from django.db import models

# Create your models here.
class DiabetesSamples(models.Model):
    sex = models.IntegerField()
    age1 = models.IntegerField()
    age2 = models.IntegerField()
    age3 = models.IntegerField()
    age4 = models.IntegerField()
    waist1 = models.IntegerField()
    waist2 = models.IntegerField()
    waist3 = models.IntegerField()
    waist4 = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    imc = models.FloatField()
    weight = models.IntegerField()
    height = models.IntegerField()
    physicalExercise = models.IntegerField()
    hypertensionPills = models.IntegerField()
    fruitsAndVegetables1 = models.IntegerField()
    fruitsAndVegetables2 = models.IntegerField()
    fruitsAndVegetables3 = models.IntegerField()
    diabeticFamily1 = models.IntegerField()
    diabeticFamily2 = models.IntegerField()
    diabeticFamily3 = models.IntegerField()
    diabeticFamily4 = models.IntegerField()
    eatsAlotFats = models.IntegerField()
    smoke1 = models.IntegerField()
    smoke2 = models.IntegerField()
    smoke3 = models.IntegerField()
    smoke4 = models.IntegerField()
    highBloodGlucose1 = models.IntegerField()
    highBloodGlucose2 = models.IntegerField()
    highBloodGlucose3 = models.IntegerField()
    glucoseAnalysis1 = models.IntegerField()
    glucoseAnalysis2 = models.IntegerField()
    glucoseLevelChange1 = models.IntegerField()
    glucoseLevelChange2 = models.IntegerField()
    glucoseLevelChange3 = models.IntegerField()
    womanGlucoseChange1 = models.IntegerField()
    womanGlucoseChange2 = models.IntegerField()
    womanGlucoseChange3 = models.IntegerField()
    womanGlucoseChange4 = models.IntegerField()
    areYouDiabetic = models.IntegerField()
    
def saveUserContribute(userContribute):
    contribute = DiabetesSamples(sex = userContribute['sex'],
    age1  =userContribute['age']['age1'],
    age2 = userContribute['age']['age2'],
    age3 = userContribute['age']['age3'],
    age4 = userContribute['age']['age4'],
    waist1  = userContribute['waist']['waist1'],
    waist2 = userContribute['waist']['waist2'],
    waist3 = userContribute['waist']['waist3'],
    waist4 = userContribute['waist']['waist4'],
    weight =  userContribute['weight'],
    height = userContribute['height'],
    imc = userContribute['imc'],
    physicalExercise = userContribute['exercise'],
    hypertensionPills = userContribute['pills'],
    fruitsAndVegetables1 =userContribute['fruits']['fruit1'],
    fruitsAndVegetables2 = userContribute['fruits']['fruit2'],
    fruitsAndVegetables3 = userContribute['fruits']['fruit3'],
    diabeticFamily1 = userContribute['diabeticFamily']['diabeticFamily1'],
    diabeticFamily2 = userContribute['diabeticFamily']['diabeticFamily2'],
    diabeticFamily3 = userContribute['diabeticFamily']['diabeticFamily3'],
    diabeticFamily4 = userContribute['diabeticFamily']['diabeticFamily4'],
    eatsAlotFats =userContribute['fats'],
    smoke1 = userContribute['smoke']['smoke1'],
    smoke2 = userContribute['smoke']['smoke2'],
    smoke3 = userContribute['smoke']['smoke3'],
    smoke4 = userContribute['smoke']['smoke4'],
    highBloodGlucose1 = userContribute['highBloodGlucose']['glucose1'],
    highBloodGlucose2 = userContribute['highBloodGlucose']['glucose2'],
    highBloodGlucose3 = userContribute['highBloodGlucose']['glucose3'],
    glucoseAnalysis1 =userContribute['glucoseAnalysis']['glucoseAnalysis1'],
    glucoseAnalysis2 =userContribute['glucoseAnalysis']['glucoseAnalysis2'],
    glucoseLevelChange1 = userContribute['glucoseLevelChange']['glucoseLevel1'],
    glucoseLevelChange2 = userContribute['glucoseLevelChange']['glucoseLevel2'],
    glucoseLevelChange3 =userContribute['glucoseLevelChange']['glucoseLevel3'],
    womanGlucoseChange1 = userContribute['womanGlucose']['womanGlucoseChange1'],
    womanGlucoseChange2 = userContribute['womanGlucose']['womanGlucoseChange2'],
    womanGlucoseChange3 = userContribute['womanGlucose']['womanGlucoseChange3'],
    womanGlucoseChange4 =userContribute['womanGlucose']['womanGlucoseChange4'],
    areYouDiabetic = userContribute['areYouDiabetic'] )

    contribute.save()
