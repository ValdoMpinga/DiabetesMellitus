from django.urls import path
from . import views

app_name = 'diabetes'

urlpatterns = [
    path('', views.diabetes, name='diabetes'),
    path('/typeone', views.diabetesOne, name='diabetes'),
    path('/typetwo', views.diabetesTwo, name='diabetes'),
    path('/gestational', views.gestationalDiabetes, name='diabetes')
]
