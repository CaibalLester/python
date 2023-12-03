from django.urls import path, include 
from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('ManageApplicant/', views.ManageApplicant, name='ManageApplicant'),
    path('ManageAgent/', views.ManageAgent, name='ManageAgent'),
    path('profile/', views.profile, name='profile'),
    path('setting/', views.setting, name='setting'),
    path('help/', views.help, name='help'),
]


