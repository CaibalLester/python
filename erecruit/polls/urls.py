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



    path('DashApp/<int:ail_id>/', views.DashApp, name='edit_ail'),

    path('delete_ail/<int:ail_id>/', views.delete_ail, name='delete_ail'),
    path('edit_ail/<int:ail_id>/', views.edit_ail, name='edit_ail'),
    
    path('DashAppp/', views.DashAppp, name='DashAppp'),
    path('DashAppp/<int:mal_id>/', views.DashAppp, name='edit_mal'),

    path('delete_mal/<int:mal_id>/', views.delete_mal, name='delete_mal'),
    path('edit_mal/<int:mal_id>/', views.edit_mal, name='edit_mal'),
    path('ManageApplicantt/', views.ManageApplicantt, name='ManageApplicantt'),

]


