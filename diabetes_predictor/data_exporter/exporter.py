import pandas as pd
import os
from django.conf import settings
from encoder.encoder import Encoder
from project_support.models import saveUserContribute

def diabetesDatasetExporter():

    df = pd.read_csv(os.path.join(
        settings.BASE_DIR, './static/dataset', 'diabetes.csv'))
    df = df[df['16. Tem diabetes?'] != "Não sei"]

    df.drop(['Carimbo de data/hora'], axis=1, inplace=True)

    for index, row in df.iterrows():

        encodedData = Encoder(1, row['1. Qual o seu sexo?'],
                         row['2. Qual a sua idade?'],
                         row['3. Qual o seu peso?'],
                         row['4. Qual a sua altura?'],
                         row['5. Qual a Medida da sua cintura?'],
                         row['6. Pratica, diariamente, atividade física com alum esforço durante pelo menos 30 minutos(ex.: no trabalho, tempo livre, caminhada, ... )?'],
                         row['7. Toma regularmente ou já tomou algum medicamento para a Hipertensão Arterial?'],
                         row['8. Com que regularidade come vegetais e/ou frutas (sopa, salada, legumes cozidos, entre outros)?'],
                         row['9. Tem algum membro de família próximo ou outros familiares a quem foi diagnosticado diabetes (Tipo 1 ou Tipo 2)?'],
                         row['10.Consome diariamente alimentos ricos em gordura (ex.: frituras, salgados, enchidos, queijos, carnes gordas)?'],
                         row['11. Você fuma?'],
                         row['12. Alguma vez teve açúcar (glicemia) elevado no sangue (ex.: num exame de saúde, durante um período de doença ou durante a gravidez)?'],
                         row['13. Quanto teve de glicose na sua última análise (mg/dL)?'],
                         row['14. Alguma vez teve alteração do seu nível de glicose?'],
                         row['15. Se mulher, alguma vez teve alteração do seu nível de glicose, diabetes durante a gravidez ou filhos com mais de 4 quilos à nascença?'],
                         row['16. Tem diabetes?']
                         )
        saveUserContribute(encodedData)
