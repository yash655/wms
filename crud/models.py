from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mob = models.IntegerField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=100)
    email = models.EmailField(('email_address'),blank=False)
    is_manager = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    
    
class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
class Worker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)    


    
