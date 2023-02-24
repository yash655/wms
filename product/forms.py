
from django import forms

from .models import *

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
        fields =["product_name","category","sale_price","avg_price","image"]        
