from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.views.generic.edit import CreateView,DeleteView,UpdateView
#from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
# Create your views here.
   
#manager requrid
class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm

    template_name = 'product/form.html'
    success_url = '/product/buyer_list.html' #add buyer list 
   
class BuyerDeleteView(DeleteView):
    model = Buyer
    template_name = 'product/delete.html'
    success_url = 'login'    

class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'product/form.html'
    success_url = 'login'
    
class BuyerrListView(ListView):
    model = Buyer
    template_name = 'product/buyer_list.html'
    buyer = Buyer.objects.all().values()
    context_object_name = 'buyer'
   
class BuyerDetailView(DetailView):
    model = Buyer
    form_class = BuyerForm
    context_object_name = 't'
    template_name = 'product/profile_detail.html'
     
      
 




          
    


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'product/form.html'
    success_url = 'login'
   
class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'product/delete.html'
    success_url = 'login'    

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'product/form.html'
    success_url = 'login'
    
class SupplierListView(ListView):
    model = Supplier
    template_name = 'product/supplier_list.html'
    supplier = Supplier.objects.all().values()
    context_object_name = 'supplier'
      
class SupplierDetailView(DetailView):
    model = Supplier
    form_class = SupplierForm
    context_object_name = 't'
    template_name = 'product/profile_detail.html'
  
      
      
      
      
      
   
class CategoryCreateView(CreateView):
    model = Category
    fields = ['id', 'c_name']
    template_name = 'product/category_form.html'
    success_url = '/crud/login'   

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product/delete.html'
    success_url = 'login' 

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['id', 'c_name']
    template_name = 'product/category_form.html'
    success_url = '/crud/login'      
 
class CategoryListView(ListView):
    model = Category
    template_name = 'product/category_list.html'
    supplier = Category.objects.all().values()
    context_object_name = 'category'
            

      
class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    # fields = '__all__'
    template_name = 'product/Product_form.html'
    success_url = '/crud/login'  
   
    
class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'product/delete.html'
    success_url = 'login'   
      
class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'product/Product_form.html'
    success_url = '/crud/login'     
       
class ProductListView(ListView):
    model = Products
    template_name = 'product/product_list.html'
    products = Products.objects.all().values()
    context_object_name = 'products'
  