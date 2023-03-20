
from django.contrib import admin
from django.urls import path,include

from . import views

from .views import *

urlpatterns = [
   
    path('BuyerCreateView/',BuyerCreateView.as_view(),name='BuyerCreateView'),
    path('BuyerUpdateView/<int:pk>',BuyerUpdateView.as_view(),name='BuyerUpdateView'),
    path('BuyerDeleteView/<int:pk>',BuyerDeleteView.as_view(),name='BuyerDeleteView'),
    path('BuyerrListView/',BuyerrListView.as_view(),name='BuyerrListView'),
    path('BuyerDetailView/<int:pk>',BuyerDetailView.as_view(),name='BuyerDetail'),



    path('SupplierCreateView/',SupplierCreateView.as_view(),name='SupplierCreateView'),
    path('SupplierUpdateView/<int:pk>',SupplierUpdateView.as_view(),name='SupplierUpdateView'),
    path('SupplierDeleteView/<int:pk>',SupplierDeleteView.as_view(),name='SupplierDeleteView'),
    path('SupplierListView/',SupplierListView.as_view(),name='SupplierListView'),  
    path('SupplierDetailView/<int:pk>',SupplierDetailView.as_view(),name='SupplierDetailView'),

    

   path('CategoryCreateView/',CategoryCreateView.as_view(),name='CategoryCreateView'),
   path('CategoryUpdateView/<int:pk>',CategoryUpdateView.as_view(),name='CategoryUpdateView'),
   path('CategoryDeleteView/<int:pk>',CategoryDeleteView.as_view(),name='CategoryDeleteView'),    
   path('CategoryListView/',CategoryListView.as_view(),name='CategoryListView'),  





   path('ProductCreateView/',ProductCreateView.as_view(),name='ProductCreateView'),
   path('ProductDeleteView/<int:pk>',ProductDeleteView.as_view(),name='ProductDeleteView'),
   path('ProductUpdateView/<int:pk>',ProductUpdateView.as_view(),name='ProductUpdateView'),
   path('ProductListView/',ProductListView.as_view(),name='ProductListView'),


   path('PurchaseCreateView/',PurchaseCreateView.as_view(),name='PurchaseCreateView'),
   path('PurchaseListView/',PurchaseListView.as_view(),name='PurchaseListView'),
   path('PurchaseDetailView/<int:pk>',PurchaseDetailView.as_view(),name='PurchaseDetailView'),
   path('PurchaseDeleteView/<int:pk>',PurchaseDeleteView.as_view(),name='PurchaseDeleteView'),
   path('PurchaseUpdateView/<int:pk>',PurchaseUpdateView.as_view(),name='PurchaseUpdateView'),




   path('SalesCreateView/',SalesCreateView.as_view(),name='SalesCreateView'),
   path('SalesListView/',SalesListView.as_view(),name='SalesListView'),
   path('SalesDetailView/<int:pk>',SalesDetailView.as_view(),name='SalesDetailView'),   
   path('SalesUpdateView/<int:pk>',SalesUpdateView.as_view(),name='SalesUpdateView'),   
   path('SalesDeleteView/<int:pk>',SalesDeleteView.as_view(),name='SalesDeleteView'),
   path('sales_update/<int:id>', views.sales_update,name='sales_update'),








   path('create_in1/<int:pk>',create_in1,name='create_in1'),
  

   path('create_in2/',create_in2,name='create_in2'),




    
]