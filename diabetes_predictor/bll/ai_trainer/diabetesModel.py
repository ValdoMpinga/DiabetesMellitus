import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os
from django.conf import settings
from sklearn.metrics import classification_report, log_loss
#Trains 1000 diabetes models, picks the best of them and saves them on the diabetes model and diabetes model backup folders
def diabetesModelTrainer(data):
    global bestModel 
    global bestModelScore 
    global bestModelScore 
    global bestModelPrecision
    global bestModelLoss

    df = pd.DataFrame(list(data))
    df.columns = df.columns.map(str)

    #Dropping unnecessary columns
    df.drop(['0'], axis=1, inplace=True)    #Id column
    df.drop(['10'], axis=1, inplace=True)   #height column
    df.drop(['11'], axis=1, inplace=True)   #weight column
    X = df.drop(['39'], axis=1).values      #finally drops also the output column (Is diabetic or not) and saves all the 
                                            #remaining columns on a X variable
    
    #Saves the output column only on a y variable
    y = df['39'].values

    model = LogisticRegression()  # Creates a logistic regression instance
    for x in range(0, 100):      #Loop to find the best logistic regression model
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        currentModel = model.fit(X_train, y_train)
        y_pred = currentModel.predict(X_train)
        pred_proba_test = model.predict_proba(X_test)
        
        currentScore = currentModel.score(X_test, y_test)
        
        report = classification_report(y_train, y_pred, output_dict=True)
        currentPrecision = report['macro avg']['precision']
        
        currentLoss =  log_loss(y_test, pred_proba_test)
        
        print("Score: ", currentScore)
        print("Precision: ", currentPrecision)
        print("Log loss on dataset test: ", currentLoss)
        
        print("Iter Score: ", currentScore)
        if x > 0 and currentScore > bestModelScore and currentPrecision > bestModelPrecision and currentLoss < bestModelLoss:
            bestModel = currentModel
            bestModelScore = currentScore
            bestModelPrecision = currentPrecision
            bestModelLoss = currentLoss
        if(x == 0):
            bestModel = currentModel
            bestModelScore = currentScore
            bestModelPrecision = currentPrecision
            bestModelLoss = currentLoss
            
  

    if bestModelScore > 0.90:
        print("Goal achieved")
        print(bestModel)
        print("Best Score: ", bestModelScore)
        print("Best Precission: ", bestModelPrecision)
        print("Best Loss: ", bestModelLoss)
    else:
        print("Goal dont achieved")
        print(bestModel)
        print("Best Score: ", bestModelScore)
        print("Best Precission: ", bestModelPrecision)
        print("Best Loss: ", bestModelLoss)
        
    #Removes the previous models on the diabetes model folder
    os.remove(os.path.join(settings.BASE_DIR, './static/diabetesModel', 'LogisticRegressionDiabetesModel'))
    
    #Removes the previous models on the diabetes model backup  folder
    os.remove(os.path.join(settings.BASE_DIR, './static/diabetesBackupModel', 'LogisticRegressionDiabetesModel'))

    #Sets model folder path
    targetPath = os.path.join( settings.BASE_DIR, './static/diabetesModel', 'LogisticRegressionDiabetesModel')
    
    #Sets backup model folder path
    targetBackupPath = os.path.join( settings.BASE_DIR, './static/diabetesBackupModel', 'LogisticRegressionDiabetesModel')
    
    #saves model
    joblib.dump(bestModel, targetPath)
    #saves backup model
    joblib.dump(bestModel, targetBackupPath)

    
