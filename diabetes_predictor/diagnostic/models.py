from django.db import models
import os
from django.conf import settings
import joblib

def predictPreview():
    row3 = [1,0,1,0,0,0.557918505,0,0,0,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0.266666667,1,0,0,0,0,1,0]
    diabetesPredictorModel = joblib.load(os.path.join(settings.BASE_DIR, './static/diabetesModel','LogisticRegressionDiabetesModel'))
    result = diabetesPredictorModel.predict_proba([row3])
    print(result)
  #  print("my base dir is : ", settings.BASE_DIR)
   # file_ = open(os.path.join(settings.BASE_DIR, './static/diabetesModel','LogisticRegressionDiabetesModel'))
    #print(file_)
    #Create your models here.
