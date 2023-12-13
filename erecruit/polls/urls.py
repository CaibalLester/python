from django.urls import path, include 
from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('ManageApplicant/', views.ManageApplicant, name='ManageApplicant'),

 

     path('DashApp/', views.DashApp, name='DashApp'),
     path('AppView/', views.AppView, name='AppView'),

]


