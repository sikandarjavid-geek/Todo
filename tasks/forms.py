from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add New Task...'}))
    
    class Meta:
        model = Tasks
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        
        model = UserProfileModel
        fields = ('profile_pic',)
