from django.urls import path
from . import views

app_name ='project_support'

urlpatterns =[
    path('', views.project_support, name='project_support'),
    path('/contribute', views.contribute, name='project_support')
]
