from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('managersignup/',ManagerSignUpView.as_view(),name='manager_signup'),    
    path('workersignup/',WorkerSignUpView.as_view(),name='worker_signup'),
    
    path('login/',UserLoginView.as_view(),name='login'),
    path('managerDashboard/',ManagerDashBoard.as_view(),name='managerdashboard'),
    path('WorkerDashBoard/',WorkerDashBoard.as_view(),name='WorkerDashBoard'),
    path('AdminDashBoard/',AdminDashBoard.as_view(),name='AdminDashBoard'),


    path('WorkerListView/',WorkerListView.as_view(),name='worker'),
    path('WorkerDeleteView/<int:pk>',WorkerDeleteView.as_view(),name='WorkerDeleteView'), 
    path('WorkerUpdateView/<int:pk>',WorkerUpdateView.as_view(),name='WorkerUpdateView'), 
    path('ManagerListView/',ManagerListView.as_view(),name='ManagerListView'), 

    


    path('dash/',views.dash,name='dash'),

    path('logout/',LogoutView.as_view(),name='logout'),

    
]