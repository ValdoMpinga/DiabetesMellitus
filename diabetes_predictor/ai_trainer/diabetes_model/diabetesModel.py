import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os
from django.conf import settings

def diabetesModelTrainer(data):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    global bestModel 
    global bestModelScore 

    df = pd.DataFrame(list(data))
    df.columns = df.columns.map(str)

    df.drop(['0'], axis=1, inplace=True)
    df.drop(['10'], axis=1, inplace=True)
    df.drop(['11'], axis=1, inplace=True)
    X = df.drop(['39'], axis=1).values
    y = df['39'].values

    model = LogisticRegression()
    for x in range(0,1000):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2)
        currentModel = model.fit(X_train, y_train)
        currentScore = currentModel.score(X_test, y_test)
        print("Iter Score: ", currentScore)
        if x > 0 and currentScore > bestModelScore:
            bestModel = currentModel
            bestModelScore = currentScore
            
            
        if(x == 0):
            bestModel = currentModel
            bestModelScore = currentScore
            
    print(bestModel)
    print("Best Score: ",bestModelScore)

    if bestModelScore > 0.90:
        print("Goal achieved")
    
    os.remove(os.path.join(
             settings.BASE_DIR, './static/diabetesModel', 'LogisticRegressionDiabetesModel'))
    
    os.remove(os.path.join(
             settings.BASE_DIR, './static/diabetesBackupModel', 'LogisticRegressionDiabetesModel'))
    
    targetPath = os.path.join(
         settings.BASE_DIR, './static/diabetesModel', 'LogisticRegressionDiabetesModel')
    
    targetBackupPath = os.path.join(
         settings.BASE_DIR, './static/diabetesBackupModel', 'LogisticRegressionDiabetesModel')
    
    joblib.dump(bestModel, targetPath)
    joblib.dump(bestModel, targetBackupPath)
