from .helpers.encoderHelper import *


def Encoder(option, sex, age, weight, height, waist, doesExercise, takePills, eatFruit, diabeticFamily, eatFats, smoke, bloodGlucose, analysis, glucoseLevelChange, womanGlucose, **diabetic):

    if(option == 1):
        # Data persistence
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
            "areYouDiabetic":     EncoderHelper.areYouDiabeticHandler(diabetic)
        }
    elif(option == 2):
        # Analysys
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


# Encoder("Masculino",
#         "Menos de 45 anos",
#         "80kg",
#         "1.70m",
#         "Homens - Menos de 94 cm | Mulheres - Menos de 80 cm",
#         "Sim",
#         "Sim",
#         "As vezes",
#         "Sim: pais, irmãos, irmãs ou filhos", "Não", "Fumo 1 a 10 cigarros por dia",
#         "Não", "400", "Não sei",
#         "Não sou mulher",
#         "Não sei")
