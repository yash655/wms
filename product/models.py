from django.db import models

class Category(models.Model):
    c_name = models.CharField(max_length=100)    
    def __str__(self):
        return self.c_name
    
    class Meta:
        db_table = 'category'



class Supplier(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100,null = True)
    email = models.EmailField()
    mob = models.IntegerField()
    gst_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.b_name
    
    class Meta:
        db_table = 'supplier'


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)
    avg_price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sale_price = models.FloatField()
    image = models.ImageField(upload_to='image/',null=True)

    def __str__(self):
        return self.p_name
    
    class Meta:
        db_table = 'product'



class Buyer(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100,null = True)
    email = models.EmailField()
    mob = models.IntegerField()
    gst_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    

    def __str__(self):
        return self.b_name
    
    class Meta:
        db_table = 'buyer'




class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField()
    dop = models.DateField()
    price =  models.FloatField()
    total =  models.FloatField()



    def __str__(self):
        return self.total
    
    class Meta:
        db_table = 'purchase'


class Sales(models.Model):
    Buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField()
    dos = models.DateField()
    price =  models.FloatField()
    total =  models.FloatField()



    def __str__(self):
        return self.total
    
    class Meta:
        db_table = 'sales'
