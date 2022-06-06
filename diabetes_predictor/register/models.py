from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserModel(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=50)
    contribuition_date = models.CharField(max_length=50,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
