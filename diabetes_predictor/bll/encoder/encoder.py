from .helpers.encoderHelper import *

#Encodes the input into binary data based on the helpers functions
def Encoder(option, sex, age, weight,
            height, waist, doesExercise, takePills,
            eatFruit, diabeticFamily, eatFats, smoke,
            bloodGlucose, analysis, glucoseLevelChange, womanGlucose, *diabetic):
    if analysis == '':
        print("Passing by")
        analysis = "Não sei"
    
    if(option == 1):#option 1 means the input is data persistence
        encoderOutput = {
            "sex": EncoderHelper.sexHandler(sex),
            "age": EncoderHelper.ageHandler(age),
            "waist": EncoderHelper.waistHandler(waist),
            "weight": EncoderHelper.weightHandler(weight),
            "height": EncoderHelper.heightHandler(height),
            "imc": EncoderHelper.imcHandler(EncoderHelper.weightHandler(
                weight), EncoderHelper.heightHandler(height)),
            "exercise": EncoderHelper.exerciseHandler(doesExercise),
            "pills":  EncoderHelper.hypertensionPills(takePills),
            "fruits": EncoderHelper.fruitsAndVagetableHandler(eatFruit),
            "diabeticFamily": EncoderHelper.diabeticFamilyHandler(diabeticFamily),
            "fats": EncoderHelper.fatsHandler(eatFats),
            "smoke": EncoderHelper.smokeHandler(smoke),
            "highBloodGlucose":     EncoderHelper.highBloodGlucoseHandler(bloodGlucose),
            "glucoseAnalysis": EncoderHelper.glucoseAnalysisHandler(analysis),
            "glucoseLevelChange": EncoderHelper.glucoseLevelChangeHandler(glucoseLevelChange),
            "womanGlucose": EncoderHelper.womanGlucoseChangeHandler(womanGlucose),
            "areYouDiabetic":  EncoderHelper.areYouDiabeticHandler(diabetic[0])
        }
    elif(option == 2):  # option 2 means the input is  the AI model evaluation
        encoderOutput = {
            "sex": EncoderHelper.sexHandler(sex),
            "age": EncoderHelper.ageHandler(age),
            "waist": EncoderHelper.waistHandler(waist),
            "imc": EncoderHelper.imcHandler(EncoderHelper.weightHandler(
                weight), EncoderHelper.heightHandler(height)),
            "exercise": EncoderHelper.exerciseHandler(doesExercise),
            "pills":  EncoderHelper.hypertensionPills(takePills),
            "fruits": EncoderHelper.fruitsAndVagetableHandler(eatFruit),
            "diabeticFamily": EncoderHelper.diabeticFamilyHandler(diabeticFamily),
            "fats": EncoderHelper.fatsHandler(eatFats),
            "smoke": EncoderHelper.smokeHandler(smoke),
            "highBloodGlucose":     EncoderHelper.highBloodGlucoseHandler(bloodGlucose),
            "glucoseAnalysis": EncoderHelper.glucoseAnalysisHandler(analysis),
            "glucoseLevelChange": EncoderHelper.glucoseLevelChangeHandler(glucoseLevelChange),
            "womanGlucose": EncoderHelper.womanGlucoseChangeHandler(womanGlucose),
        }

    return encoderOutput
