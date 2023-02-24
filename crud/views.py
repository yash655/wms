from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import *
from .models import User
from .forms import *
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class ManagerSignUpView(CreateView):
    model = User
    form_class =ManagerSignUpForm
    template_name = 'template/html/auth-register-basic.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    
    
    
    def form_valid(self,form):
         user = form.save()
       
         email = form.cleaned_data.get('email')
       
         res = sendMail(email)
         if res>0:
            login(self.request,user)

         return redirect('login')
  
  
  
class WorkerSignUpView(CreateView):
    model = User
    form_class =WorkerSignUpForm
    template_name = 'template/html/auth-register-basic.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'worker'
        return super().get_context_data(**kwargs)
    
    
    def form_valid(self,form):
         user = form.save()
       
         email = form.cleaned_data.get('email')
       
         res = sendMail(email)
         if res>0:
            login(self.request,user)

         return redirect('Signupman')



  

class UserLoginView(LoginView):
    template_name = 'template/html/auth-login-basic.html'
    
    def get_redirect_url(self):    
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/crud/managerDashboard/'
            else:
                return '/cbv/contactlist/'
    def get(self, request, *args, **kwargs):
        
        return self.render_to_response(self.get_context_data())
    
class ManagerDashBoard(ListView):
    template_name ="product/index.html"
    context_object_name = "managaer"
    model = User
    

def sendMail(mailid):
    subject = 'Welcome to our site'
    message = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mailid]
    res = send_mail(subject,message,email_from,recipient_list)
    print(res)
    return res      

   