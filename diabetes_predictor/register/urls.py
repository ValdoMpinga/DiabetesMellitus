from django.urls import path
from . import views

urlpatterns =[
    path('', views.register, name='register'),
    path('/activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]
