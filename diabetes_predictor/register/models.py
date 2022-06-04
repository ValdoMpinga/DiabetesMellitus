from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=30)
  
    
def createUser(firstName):
    user =User(firstName=firstName)
    user.save()
