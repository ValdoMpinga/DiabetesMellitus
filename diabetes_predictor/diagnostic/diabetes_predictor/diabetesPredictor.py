from cmath import log
import os
from django.conf import settings
import joblib
from encoder.encoder import Encoder
from typing import Iterable

# from ...encoder.encoder import Encoder

diabetesPredictorModel = joblib.load(os.path.join(
    settings.BASE_DIR, './static/diabetesModel', 'LogisticRegressionDiabetesModel'))


def Predict(data):

    # encodedSample=Encoder()
   # print(data)
    sampleArray = []
    encondedSample = Encoder(2, data['sex'],
                             data['age'],
                             data['weight'],
                             data['height'],
                             data['waist'],
                             data['exercise'],
                             data['pills'],
                             data['fruits'],
                             data['diabeticFamily'],
                             data['fats'],
                             data['smoke'],
                             data['highBloodGlucose'],
                             data['glucoseAnalysis'],
                             data['glucoseLevelChange'],
                             data['womanGlucose'],
                             )

    # print(encondedSample)
    for key, value in recursive_items(encondedSample):
        sampleArray.append(value)

   # print(sampleArray)
    predictionOutput = getPrediction(sampleArray)
    predictionProbabilityOutput = getPredictionProbability(
        sampleArray, predictionOutput)

    return ([predictionOutput, predictionProbabilityOutput])


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)


def getPrediction(sampleArray):
    prediction = diabetesPredictorModel.predict([sampleArray])
    parsedPredictionValue = int(prediction.tolist()[0])
    print(parsedPredictionValue)
    return parsedPredictionValue


def getPredictionProbability(sampleArray, prediction):
    prediction_probability = diabetesPredictorModel.predict_proba([sampleArray])

    parserPrediction_probability = prediction_probability.tolist()
    parsedArray = parserPrediction_probability[0]

    if prediction == 0:
        return parsedArray[0]
    else:
        return parsedArray[1]
