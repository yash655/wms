from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import *
from django.views.generic.edit import CreateView,DeleteView,UpdateView
#from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
   
#manager requrid
class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm

    template_name = 'product/form.html'
    success_url = '/product/BuyerrListView'  
   
class BuyerDeleteView(DeleteView):
    model = Buyer
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/product/BuyerrListView'  

class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'product/form.html'
    success_url = '/product/BuyerrListView'  
    
class BuyerrListView(ListView):
    model = Buyer
    template_name = 'product/buyer_list.html'
    buyer = Buyer.objects.all().values()
    context_object_name = 'buyer'
   
class BuyerDetailView(DetailView):
    model = Buyer
    form_class = BuyerForm
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
       
        buyer = self.object
        sales = buyer.sales_set.all()
        context['sales'] = sales
        return context


    template_name = 'product/profile_detail.html'
     
      
 




          
    


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'product/form.html'
    success_url = '/product/SupplierListView'  
   
class SupplierDeleteView(DeleteView):
    model = Supplier
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)   
    success_url = '/product/SupplierListView'  

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'product/form.html'
    success_url = '/product/SupplierListView'  
    
class SupplierListView(ListView):
    model = Supplier
    template_name = 'product/supplier_list.html'
    supplier = Supplier.objects.all().values()
    context_object_name = 'supplier'
      
class SupplierDetailView(DetailView):
    model = Supplier
    form_class = SupplierForm
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
       
        Supplier = self.object
        Purchase = Supplier.purchase_set.all()
        context['Purchase'] = Purchase
        return context    
    template_name = 'product/profile_detail_supplier.html'
  
      
      
      
      
      
   
class CategoryCreateView(CreateView):
    model = Category
    fields = ['id', 'c_name','icon']
    template_name = 'product/category_form.html'
    success_url = '/product/CategoryListView'  

class CategoryDeleteView(DeleteView):
    model = Category
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)    
    success_url = '/product/CategoryListView'  

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['id', 'c_name','icon']
    template_name = 'product/category_form.html'
    success_url = '/product/CategoryListView'  
 
class CategoryListView(ListView):
    model = Category
    template_name = 'product/category_list.html'
    category = Category.objects.all().values()
    context_object_name = 'category'
            

      
class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    # fields = '__all__'
    template_name = 'product/Product_form.html'
    success_url = '/product/ProductListView'  
   
    
class ProductDeleteView(DeleteView):
    model = Products
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/product/ProductListView'  
      
class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'product/Product_form.html'
    success_url = '/product/ProductListView'  
       
class ProductListView(ListView):
    model = Products
    template_name = 'product/product_list.html'
    products = Products.objects.all().values()
    context_object_name = 'products'
  
  
class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    # fields = '__all__'
    def form_valid(self, form):
        # Modify the form data here
        form.instance.user = self.request.user
        product = form.cleaned_data['products']
       
        p = Products.objects.get(product_name=product)
       
        qty = form.cleaned_data['qty']
        pq = Products.objects.filter(product_name=product).update(qty=p.qty+qty )

        form.instance.total = p.avg_buy_price  * qty
        #q = form.cleaned_data.get('qty')
        # Call the parent form_valid() method to save the object to the database
        return super().form_valid(form) 
  



    template_name = 'product/purchase_form.html'
    success_url = '/product/PurchaseListView'  
   
   
def create_in1(request, pk):
    supplier = Supplier.objects.get(id=pk)
    purchase = Purchase.objects.filter(supplier=supplier)
    formset = PurchaseFormSet(request.POST or None)
    if request.method == "POST":

    
        formset.instance = supplier
        formset.save()
        return redirect('/product/create_in1/',pk=supplier.id)
        
    context = {
        "formset": formset,
        "supplier": supplier,
        "purchase": purchase
    }

    return render(request, "partials/createpurchase_form.html", context)


def create_in2(request):
    form = PurchaseForm()
    context = {
        "form": form
    }
    return render(request, "partials/purchase_form.html", context)


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'product/Purchase_list.html'
    purchase = Purchase.objects.all().values()
    context_object_name = 'purchase'
  

class PurchaseDetailView(DetailView):
    model = Purchase
    form_class = PurchaseForm
    context_object_name = 'form'
    template_name = 'product/purchase_detail.html'
  
  
class PurchaseDeleteView(DeleteView):
    model = Purchase
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/product/PurchaseListView'  

class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'product/purchase_form.html'
    success_url = '/product/PurchaseListView'  
     
  
  
class SalesCreateView(CreateView):
    model = Sales
    form_class = SalesForm
    # fields = '__all__'
    def form_valid(self, form):
        # Modify the form data here
        form.instance.user = self.request.user
        product = form.cleaned_data['products']
       
        p = Products.objects.get(product_name=product)
       
        qty = form.cleaned_data['qty']
        pq = Products.objects.filter(product_name=product).update(qty=p.qty-qty )

        form.instance.total = p.sale_price  * qty
        #q = form.cleaned_data.get('qty')
        # Call the parent form_valid() method to save the object to the database
        return super().form_valid(form) 
  



    template_name = 'product/Sales_form.html'
    success_url = '/product/SalesListView'  
 
 
 
class SalesListView(ListView):
    model = Sales
    
    template_name = 'product/Sales_list.html'
    sales = Sales.objects.all().values()
    context_object_name = 'sales'
  

class SalesDetailView(DetailView):
    model = Sales
    form_class = SalesForm
    context_object_name = 'form'
    template_name = 'product/Sales_detail.html'
  
  
class SalesDeleteView(DeleteView):
    model = Sales
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/product/SalesListView'  

class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'product/Sales_form.html'
    success_url = '/product/SalesListView'  
     
def sales_update(request,id):
    sales = Sales.objects.filter(id=id).update(Status='Dispatch ')
    return HttpResponseRedirect('/product/SalesListView')

