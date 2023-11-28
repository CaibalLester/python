from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),




    path('dashboard/', views.dashboard),
    path('ManageApplicant/', views.ManageApplicant),
    path('ManageAgent/', views.ManageAgent),

]