from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import *
from .models import User
from .forms import *
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from product.models import *
from django.db.models import *
from django.urls import reverse_lazy


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
         print(email)
         res = sendMail(email)
         if res>0:
            login(self.request,user)

         return redirect('login')



  

class UserLoginView(LoginView):
    template_name = 'template/html/auth-login-basic.html'
    # template_name = 'product/profile_user_changes.html'


    
    def get_redirect_url(self):    
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/crud/managerDashboard/'
            elif self.request.user.is_superuser:
                return '/crud/AdminDashBoard/'
            else:
                return '/crud/WorkerDashBoard/'
    def get(self, request, *args, **kwargs):
        
        return self.render_to_response(self.get_context_data())

class AdminDashBoard(ListView):


   
    def get(self, request, *args, **kwargs):
        product = Products.objects.all().values()
        category = Category.objects.all().values()
        buyer = Buyer.objects.all().values()
        supplier = Supplier.objects.all().values()
        qty = Sales.objects.aggregate(total1 = Sum('qty'),tsales = Sum('total'),trn = Max('id') )
        pur = Purchase.objects.aggregate(totalpur = Max('id'))
        x = Products.objects.aggregate(tqty = Sum('qty'))

        
        return render(request, 'product/admin_dashboard.html', {'pur':pur,'x':x,'qty':qty,'product':product, 'category':category,'buyer':buyer,'supplier':supplier}) 

    
class ManagerDashBoard(ListView):


   
   def get(self, request, *args, **kwargs):
        product = Products.objects.all().values()
        category = Category.objects.all().values()
        buyer = Buyer.objects.all().values()
        supplier = Supplier.objects.all().values()
        qty = Sales.objects.aggregate(total1 = Sum('qty'),tsales = Sum('total'),trn = Max('id') )
        pur = Purchase.objects.aggregate(totalpur = Max('id'))
        x = Products.objects.aggregate(tqty = Sum('qty'))

        
        return render(request, 'product/manager_dashbord.html', {'pur':pur,'x':x,'qty':qty,'product':product, 'category':category,'buyer':buyer,'supplier':supplier}) 

 
class WorkerDashBoard(ListView):


   
    def get(self, request, *args, **kwargs):
        product = Products.objects.all().values()
        category = Category.objects.all().values()
        buyer = Buyer.objects.all().values()
        supplier = Supplier.objects.all().values()
        
        print(Sales.objects.aggregate(total = Sum('qty')))
        
        return render(request, 'product/worker_dashborad.html', {'product':product, 'category':category,'buyer':buyer,'supplier':supplier}) 


def sendMail(mailid):
    subject = 'Welcome to our site'
    message = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mailid]
    res = send_mail(subject,message,email_from,recipient_list)
    return res      

   
class WorkerListView(ListView):
    model = User
    template_name = 'product/worker_list.html'
    def get_queryset(self) :
        worker1 = User.objects.filter(is_worker = True).values()
        return worker1
    context_object_name = 'worker1'
     
class WorkerDeleteView(DeleteView):
    model = User
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/crud/WorkerListView'  
   
   
class WorkerUpdateView(UpdateView):
    model = User
    fields = ['username','email']
    template_name = 'template/html/auth-register-basic1.html'
    success_url = '/crud/WorkerListView'  


   
class ManagerListView(ListView):
    model = User
    template_name = 'product/worker_list.html'
    def get_queryset(self) :
        worker1 = User.objects.filter(is_manager = True).values()
        return worker1
    context_object_name = 'worker1'
     
     

def dash(request):
     if request.user.is_authenticated:
            print('hello')
            if request.user.is_manager:
                print('hellooo')
                return HttpResponseRedirect('/crud/managerDashboard/')

            elif request.user.is_superuser:
                return HttpResponseRedirect('/crud/AdminDashBoard/')

            else:
                return HttpResponseRedirect('/crud/WorkerDashBoard/')



class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'product/profile_user_changes.html'
    def get_success_url(self):
        return reverse_lazy('UserDetailView', kwargs={'pk': self.object.pk}) 
    
    
class UserDetailView(DetailView):
    model = User
    form_class = UserUpdateForm
    context_object_name = 'form'
    template_name = 'product/profile_user.html'