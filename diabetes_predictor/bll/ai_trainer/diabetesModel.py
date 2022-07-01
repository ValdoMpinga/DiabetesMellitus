import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os
import pickle
from datetime import datetime
from django.conf import settings
from sklearn.metrics import classification_report, log_loss, confusion_matrix
from django.core.mail import send_mail
from project_support.models import DiabetesSamples
from ai_model_history.models import AI_ModelHistory
# Trains 1000 diabetes models, picks the best of them and saves them on the diabetes model and diabetes model backup folders

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def diabetesModelTrainer():
    data = DiabetesSamples.objects.all().values_list()
    global bestModel
    global bestModelScore
    global bestModelScore
    global bestModelPrecision
    global bestModelLoss

    df = pd.DataFrame(list(data))
    df.columns = df.columns.map(str)

    # Dropping unnecessary columns
    df.drop(['0'], axis=1, inplace=True)  # Id column
    df.drop(['10'], axis=1, inplace=True)  # height column
    df.drop(['11'], axis=1, inplace=True)  # weight column
    # finally drops also the output column (Is diabetic or not) and saves all the
    X = df.drop(['39'], axis=1).values
    # remaining columns on a X variable

    # Saves the output column only on a y variable
    y = df['39'].values

    model = LogisticRegression()  # Creates a logistic regression instance
    for x in range(0, 100):  # Loop to find the best logistic regression model

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        currentModel = model.fit(X_train, y_train)
        y_pred = currentModel.predict(X_train)
        pred_proba_test = model.predict_proba(X_test)

        report = classification_report(y_train, y_pred, output_dict=True)
        
        currentScore = currentModel.score(X_test, y_test)
        currentPrecision = report['macro avg']['precision']
        currentLoss = log_loss(y_test, pred_proba_test)
        
        print(confusion_matrix_calculator(y_train, y_pred))
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
            

    bestModelScore = bestModelScore * 100
    bestModelPrecision = bestModelPrecision * 100
    bestModelLoss = bestModelLoss * 100

    if bestModelScore > 0.90:
        binaryModel = pickle.dumps(bestModel)
        print(bcolors.OKGREEN + "Goal achieved" + bcolors.ENDC)
        print(bestModel)
        print("Best Score: ", bestModelScore)
        print("Best Precission: ", bestModelPrecision)
        print("Best Loss: ", bestModelLoss)
        print(confusion_matrix_calculator(y_train, y_pred))
        
        aiModelHistoryInstance = AI_ModelHistory(algorithm="Logistic Regression",
            score=bestModelScore, 
            precison=bestModelPrecision, 
            loss=bestModelLoss,
            confusion_matrix=confusion_matrix_calculator(y_train, y_pred),
            model=binaryModel,
            inserted_on=datetime.now())
        aiModelHistoryInstance.save()

        send_mail('Relatorio do re treino da IA',
                  'A IA de diabetes foi re treinada com sucesso, com uma pontuação de {} %, uma precisão de {} % e perca de {} %'.format(
                      int(bestModelScore), int(bestModelPrecision), round(bestModelLoss, 2)),
                  settings.EMAIL_HOST_USER,
                  ['valdom@ipvc.pt'],
                  fail_silently=False)

    else:
        binaryModel = pickle.dumps(bestModel)
        print(bcolors.WARNING + "Goal wasn't achieved"  + bcolors.ENDC)
        print(bestModel)
        print("Best Score: ", bestModelScore)
        print("Best Precission: ", bestModelPrecision)
        print("Best Loss: ", bestModelLoss)
        print(confusion_matrix_calculator(y_train, y_pred)) 
        
        aiModelHistoryInstance = AI_ModelHistory(algorithm="Logistic Regression",
            score=bestModelScore, 
            precison=bestModelPrecision, 
            loss=bestModelLoss,
            confusion_matrix=confusion_matrix_calculator(y_train, y_pred),
            model=binaryModel,
            inserted_on=datetime.now())
        aiModelHistoryInstance.save()

        send_mail('Relatorio do re treino da IA',
                  'A IA de diabetes foi re treinada, porem sem sucesso, com uma pontuação de {} , uma precisão de {} e perca de {} '.format(
                      bestModelScore, bestModelPrecision, bestModelLoss),
                  settings.EMAIL_HOST_USER,
                  ['valdom@ipvc.pt'],
                  fail_silently=False)

    # Removes the previous models on the diabetes model folder
    os.remove(os.path.join(settings.BASE_DIR,
              './static/diabetesModel', 'LogisticRegressionDiabetesModel'))

    # Removes the previous models on the diabetes model backup  folder
    os.remove(os.path.join(settings.BASE_DIR,
              './static/diabetesBackupModel', 'LogisticRegressionDiabetesModel'))

    # Sets model folder path
    targetPath = os.path.join(
        settings.BASE_DIR, './static/diabetesModel', 'LogisticRegressionDiabetesModel')

    # Sets backup model folder path
    targetBackupPath = os.path.join(
        settings.BASE_DIR, './static/diabetesBackupModel', 'LogisticRegressionDiabetesModel')

    # saves model
    joblib.dump(bestModel, targetPath)
    # saves backup model
    joblib.dump(bestModel, targetBackupPath)


def confusion_matrix_calculator(y_train, y_pred):
        cm = confusion_matrix(y_train, y_pred)
        cm_norm = cm / cm.sum(axis=1).reshape(-1, 1)
        
        confusion_matriz_dict = {
            "true_positive": cm_norm[0][0],
            "false_positive": cm_norm[0][1],
            "false_negative": cm_norm[1][0],
            "true_negative": cm_norm[1][1],
        }
        
        return confusion_matriz_dict
