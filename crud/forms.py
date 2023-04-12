from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction
from django import forms


class ManagerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user
    
    
class WorkerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_worker = True
        user.save()
        return user
    
    
class UserUpdateForm(forms.ModelForm):
     class Meta:
        model = User
        fields =["username","first_name","last_name","email","mob","address"]
        widgets = {
            'address': forms.Textarea(attrs={"rows":3, "cols":10})
        }