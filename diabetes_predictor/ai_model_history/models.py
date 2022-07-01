from django.db import models

# Create your models here.
class AI_ModelHistory(models.Model):
    algorithm = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=30, decimal_places=1)
    precison = models.DecimalField(max_digits=30, decimal_places=1)
    loss = models.DecimalField(max_digits=30, decimal_places=1)
    confusion_matrix = models.TextField(max_length=150)
    model = models.BinaryField()
    inserted_on = models.DateField()
