from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('login', views.login),
    path('register', views.registrationPage, name='registration'),
]