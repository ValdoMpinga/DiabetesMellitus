import re
from enum import Enum
from helpers.encoderEnumerations import *


class EncoderHelper():
    def sexHandler(sex):
        try:
            if(sex == SexEnum.male.value):
                return 1
            elif (sex == SexEnum.female.value):
                return 0
        except:
            print("Please check if you inserted the right values")

    def ageHandler(age):
        try:
            ageObject = {
                'age1': 0,
                'age2': 0,
                'age3': 0,
                'age4': 0,
            }

            if(age == AgeEnum.ageBellow45.value):
                ageObject['age1'] = 1
                ageObject['age2'] = 0
                ageObject['age3'] = 0
                ageObject['age4'] = 0
            elif(age == AgeEnum.ageBetween45And54.value):
                ageObject['age1'] = 0
                ageObject['age2'] = 1
                ageObject['age3'] = 0
                ageObject['age4'] = 0
            elif(age == AgeEnum.ageBetween45And54.value):
                ageObject['age1'] = 0
                ageObject['age2'] = 0
                ageObject['age3'] = 1
                ageObject['age4'] = 0
            elif(age == AgeEnum.ageAbove64.value):
                ageObject['age1'] = 0
                ageObject['age2'] = 0
                ageObject['age3'] = 0
                ageObject['age4'] = 1

            return ageObject
        except:
            print("Please check if you inserted the right values")

    def weightHandler(weight):
        try:
            finalWeight = re.sub('\D', '', weight)
            return finalWeight
        except:
            print("Please check if you inserted the right values")

    def heightHandler(height):
        try:
            finalHeight = re.sub('\D', '', height)
            finalHeight = int(finalHeight)/100

            if finalHeight < 1:
                finalHeight += 1
            elif finalHeight >= 10:
                finalHeight /= 10

            return finalHeight
        except:
            print("Please check if you inserted the right values")

    def waistHandler(waist):
        try:
            waistObject = {
                'waist1': 0,
                'waist2': 0,
                'waist3': 0,
                'waist4': 0,
            }

            if(waist == WaistEnum.waistCategoryOne.value):
                waistObject['waist1'] = 1
                waistObject['waist2'] = 0
                waistObject['waist3'] = 0
                waistObject['waist4'] = 0
            elif(waist == WaistEnum.waistCategoryTwo.value):
                waistObject['waist1'] = 0
                waistObject['waist2'] = 1
                waistObject['waist3'] = 0
                waistObject['waist4'] = 0
            elif(waist == WaistEnum.waistCategoryThree.value):
                waistObject['waist1'] = 0
                waistObject['waist2'] = 0
                waistObject['waist3'] = 1
                waistObject['waist4'] = 0
            elif(waist == WaistEnum.waistCategoryUnkown.value):
                waistObject['waist1'] = 0
                waistObject['waist2'] = 0
                waistObject['waist3'] = 0
                waistObject['waist4'] = 1

            return waistObject
        except:
            print("Please check if you inserted the right values")

    def imcHandler(weight, height):
        try:
            weight = float(weight)
            height = float(height)
            imc = (weight / (height * height))/45
            if imc > 1:
                return 1
            elif imc <= 1:
                return 0
            else:
                print("Imc:" + imc)
        except:
            print("Please check if you inserted the right values")

    def exerciseHandler(doesExercise):
        try:
            if(doesExercise == ExerciseEnum.yes.value):
                return 1
            elif (doesExercise == ExerciseEnum.no.value):
                return 0
        except:
            print("Please check if you inserted the right values")

    def hypertensionPills(takePills):
        try:
            if(takePills == HypertensionEnum.yes.value):
                return 1
            elif (takePills == HypertensionEnum.no.value):
                return 0
        except:
            print("Please check if you inserted the right values")

    def fruitsAndVagetableHandler(eatFuit):
        try:
            fruitObject = {
                'fruit1': 0,
                'fruit2': 0,
                'fruit3': 0,
            }

            if(eatFuit == FruitsAndVegetablesEnum.everyDay.value):
                fruitObject['fruit1'] = 1
                fruitObject['fruit2'] = 0
                fruitObject['fruit3'] = 0
            elif(eatFuit == FruitsAndVegetablesEnum.sometimes.value):
                fruitObject['fruit1'] = 0
                fruitObject['fruit2'] = 1
                fruitObject['fruit3'] = 0
            elif(eatFuit == FruitsAndVegetablesEnum.dontEat.value):
                fruitObject['fruit1'] = 0
                fruitObject['fruit2'] = 0
                fruitObject['fruit3'] = 1

            return fruitObject
        except:
            print("Please check if you inserted the right values")

    def diabeticFamilyHandler(diabeticFamily):
        try:
            diabeticFamilyObject = {
                'diabeticFamily1': 0,
                'diabeticFamily2': 0,
                'diabeticFamily3': 0,
                'diabeticFamily4': 0,
            }

            if(diabeticFamily == DiabeticFamilyEnum.yesExceptParents.value):
                diabeticFamilyObject['diabeticFamily1'] = 1
                diabeticFamilyObject['diabeticFamily2'] = 0
                diabeticFamilyObject['diabeticFamily3'] = 0
                diabeticFamilyObject['diabeticFamily4'] = 0
            elif(diabeticFamily == DiabeticFamilyEnum.yesParents.value):
                diabeticFamilyObject['diabeticFamily1'] = 0
                diabeticFamilyObject['diabeticFamily2'] = 1
                diabeticFamilyObject['diabeticFamily3'] = 0
                diabeticFamilyObject['diabeticFamily4'] = 0
            elif(diabeticFamily == DiabeticFamilyEnum.no.value):
                diabeticFamilyObject['diabeticFamily1'] = 0
                diabeticFamilyObject['diabeticFamily2'] = 0
                diabeticFamilyObject['diabeticFamily3'] = 1
                diabeticFamilyObject['diabeticFamily4'] = 0
            elif(diabeticFamily == DiabeticFamilyEnum.dontKnow.value):
                diabeticFamilyObject['diabeticFamily1'] = 0
                diabeticFamilyObject['diabeticFamily2'] = 0
                diabeticFamilyObject['diabeticFamily3'] = 0
                diabeticFamilyObject['diabeticFamily4'] = 1

            return diabeticFamilyObject
        except:
            print("Please check if you inserted the right values")

    def fatsHandler(eatFats):
        try:
            if (eatFats == EatsAlotFatsEnum.yes.value):
                return 1
            elif(eatFats == EatsAlotFatsEnum.no.value):
                return 0
        except:
            print("Please check if you inserted the right values")

    def smokeHandler(smoke):
        try:
            smokeObject = {
                'smoke1': 0,
                'smoke2': 0,
                'smoke3': 0,
                'smoke4': 0,
            }

            if(smoke == SmokeEnum.no.value):
                smokeObject['smoke1'] = 1
                smokeObject['smoke2'] = 0
                smokeObject['smoke3'] = 0
                smokeObject['smoke4'] = 0
            elif(smoke == SmokeEnum.yesButStoped.value):
                smokeObject['smoke1'] = 0
                smokeObject['smoke2'] = 1
                smokeObject['smoke3'] = 0
                smokeObject['smoke4'] = 0
            elif(smoke == SmokeEnum.yesOneToTenAday.value):
                smokeObject['smoke1'] = 0
                smokeObject['smoke2'] = 0
                smokeObject['smoke3'] = 1
                smokeObject['smoke4'] = 0
            elif(smoke == SmokeEnum.yesMoreThenTenAday.value):
                smokeObject['smoke1'] = 0
                smokeObject['smoke2'] = 0
                smokeObject['smoke3'] = 0
                smokeObject['smoke4'] = 1

            return smokeObject
        except:
            print("Please check if you inserted the right values")

    def highBloodGlucoseHandler(bloodGlucose):
        try:
            highBloodGlucoseObject = {
                'glucose1': 0,
                'glucose2': 0,
                'glucose3': 0,
            }

            if(bloodGlucose == highBloodGlucoseEnum.yes.value):
                highBloodGlucoseObject['glucose1'] = 1
                highBloodGlucoseObject['glucose2'] = 0
                highBloodGlucoseObject['glucose3'] = 0
            elif(bloodGlucose == highBloodGlucoseEnum.no.value):
                highBloodGlucoseObject['glucose1'] = 0
                highBloodGlucoseObject['glucose2'] = 1
                highBloodGlucoseObject['glucose3'] = 0
            elif(bloodGlucose == highBloodGlucoseEnum.dontKnow.value):
                highBloodGlucoseObject['glucose1'] = 0
                highBloodGlucoseObject['glucose2'] = 0
                highBloodGlucoseObject['glucose3'] = 1

            return highBloodGlucoseObject
        except:
            print("Please check if you inserted the right values")

    def glucoseAnalysisHandler(analysis):
        try:

            glucoseAnalysisObject = {
                'glucoseAnalysis1': 0,
                'glucoseAnalysis2': 0,
            }

            if(analysis == GlucoseAnalysisEnum.dontKnow.value):
                glucoseAnalysisObject['glucoseAnalysis1'] = 1
                glucoseAnalysisObject['glucoseAnalysis2'] = 0
            else:
                analysisResult = re.sub('\D', '', analysis)
                analysisResult = int(analysisResult)
                glucoseAnalysisObject['glucoseAnalysis1'] = 1
                if analysisResult/450 > 1:
                    glucoseAnalysisObject['glucoseAnalysis2'] = 1
                else:
                    glucoseAnalysisObject['glucoseAnalysis2'] = 0

            return glucoseAnalysisObject
        except:
            print("Please check if you inserted the right values")

    def glucoseLevelChangeHandler(glucoseChange):
        try:
            glucoseLeveleObject = {
                'glucoseLevel1': 0,
                'glucoseLevel2': 0,
                'glucoseLevel3': 0,
            }

            if(glucoseChange == GlucoseLevelChangeEnum.yes.value):
                glucoseLeveleObject['glucoseLevel1'] = 1
                glucoseLeveleObject['glucoseLevel2'] = 0
                glucoseLeveleObject['glucoseLevel3'] = 0
            elif(glucoseChange == GlucoseLevelChangeEnum.no.value):
                glucoseLeveleObject['glucoseLevel1'] = 0
                glucoseLeveleObject['glucoseLevel2'] = 1
                glucoseLeveleObject['glucoseLevel3'] = 0
            elif(glucoseChange == GlucoseLevelChangeEnum.dontKnow.value):
                glucoseLeveleObject['glucoseLevel1'] = 0
                glucoseLeveleObject['glucoseLevel2'] = 0
                glucoseLeveleObject['glucoseLevel3'] = 1

            return glucoseLeveleObject
        except:
            print("Please check if you inserted the right values")

    def womanGlucoseChangeHandler(womanGlucose):
        try:
            woamnGlucoseObject = {
                'womanGlucoseChange1': 0,
                'womanGlucoseChange2': 0,
                'womanGlucoseChange3': 0,
                'womanGlucoseChange4': 0,
            }

            if(womanGlucose == WomanGlucoseChangeEnum.yes.value):
                woamnGlucoseObject['womanGlucoseChange1'] = 1
                woamnGlucoseObject['womanGlucoseChange2'] = 0
                woamnGlucoseObject['womanGlucoseChange3'] = 0
                woamnGlucoseObject['womanGlucoseChange4'] = 0
            elif(womanGlucose == WomanGlucoseChangeEnum.no.value):
                woamnGlucoseObject['womanGlucoseChange1'] = 0
                woamnGlucoseObject['womanGlucoseChange2'] = 1
                woamnGlucoseObject['womanGlucoseChange3'] = 0
                woamnGlucoseObject['womanGlucoseChange4'] = 0
            elif(womanGlucose == WomanGlucoseChangeEnum.notAWoman.value):
                woamnGlucoseObject['womanGlucoseChange1'] = 0
                woamnGlucoseObject['womanGlucoseChange2'] = 0
                woamnGlucoseObject['womanGlucoseChange3'] = 1
                woamnGlucoseObject['womanGlucoseChange4'] = 0
            elif(womanGlucose == highBloodGlucoseEnum.dontKnow.value):
                woamnGlucoseObject['womanGlucoseChange1'] = 0
                woamnGlucoseObject['womanGlucoseChange2'] = 0
                woamnGlucoseObject['womanGlucoseChange3'] = 0
                woamnGlucoseObject['womanGlucoseChange4'] = 1

            return woamnGlucoseObject
        except:
            print("Please check if you inserted the right values")

    def areYouDiabeticHandler(diabetic):
        try:
            AreYouDiabetic = 0
            if(diabetic == AreYouDiabeticEnum.yes.value):
                AreYouDiabetic = 1
            elif(diabetic == AreYouDiabeticEnum.no.value):
                AreYouDiabetic = 0
            elif(diabetic == AreYouDiabeticEnum.dontKnow.value):
                AreYouDiabetic = 0

            return AreYouDiabetic
        except:
            print("Please check if you inserted the right values")


# class Age(Enum):
#     ageBellow45 = "Menos de 45 anos"
#     ageBetween45And54 = "45-54 anos"
#     ageBetween55And64 = "55-64 anos"
#     ageAbove64 = "Mais de 64 anos"
