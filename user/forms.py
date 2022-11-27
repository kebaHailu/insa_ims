from django import forms 
from .models import Profile 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
    def __init__(self,*args,**kwargs):
        super(CreateUserForm,self).__init__(*args,**kwargs)
        
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None 
        
class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields =['address','phone','image']