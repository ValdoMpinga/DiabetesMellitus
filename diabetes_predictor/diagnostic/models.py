from django.db import models
import os
from django.conf import settings
import joblib

class DiagnosticSample(models.Model):

    sex_choices = (('Masculino', 'Masculino'), ('Feminino', 'Feminino'))
    sexo = models.TextField(choices=sex_choices, default='Feminino')
    peso = models.CharField(max_length=10)
    altura = models.CharField(max_length=10)
    glicemia = models.CharField(max_length=10)
    data = models.DateField()
