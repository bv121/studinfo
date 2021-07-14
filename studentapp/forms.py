from django import forms
from .models import UserInfo,Student,User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
         model=UserInfo
         fields=['username','first_name','last_name','gender','age','email','contact','password1','password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)