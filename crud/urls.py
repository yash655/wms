from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('managersignup/',ManagerSignUpView.as_view(),name='manager_signup'),    
    path('workersignup/',WorkerSignUpView.as_view(),name='worker_signup'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('managerDashboard/',ManagerDashBoard.as_view(),name='managerdashboard'),
    path('logout/',LogoutView.as_view(),name='logout'),

    
]