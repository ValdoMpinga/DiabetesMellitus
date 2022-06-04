from django.urls import path
from . import views

app_name ='diagnostic'

urlpatterns =[
    path('', views.diagnostic, name='diagnostic')
]
