from django.urls import path
from . import views

urlpatterns = [
    path('/', views.diabetes, name='diabetes'),
    path('/typeone/', views.diabetesOne, name='diabetes1'),
    path('/typetwo/', views.diabetesTwo, name='diabetes2'),
    path('/gestational/', views.gestationalDiabetes, name='diabetesgestational')
]
