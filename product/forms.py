
from django import forms
from django.db import transaction

from .models import *
from django.forms.models import (
    inlineformset_factory, 
    formset_factory, 
    modelform_factory, 
    modelformset_factory
)
class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields =["name","company_name","email","mob","gst_no","address"]
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields =["name","company_name","email","mob","gst_no","address"]
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =["product_name","category","qty","sale_price","avg_buy_price","image"]        
    # @transaction.atomic
    # def save(self):
    #     Products = super().save(commit=False)
    #     print(self.request.user,'hello')
    #     Products.updatedby = self.request.user
        
    #     Products.save()
    #     return Products

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields =["supplier","products","qty","total"]    
           


PurchaseFormSet = inlineformset_factory(
    Supplier,
    Purchase,
    form=PurchaseForm,
    min_num=2,  # minimum number of forms that must be filled in
    extra=1,  # number of empty forms to display
    can_delete=False  # show a checkbox in each form to delete the row
)

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields =["Buyer","products","qty","total"]    
 