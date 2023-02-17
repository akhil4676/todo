from dataclasses import fields
from django import forms
from myapp.models import Todos
from django.contrib.auth.models import User

class TodoForm(forms.Form):
    task_name=forms.CharField(label="enter task name",required=True)
    user=forms.CharField(label="user name",required=True)

class TodoModelForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["task_name"]


        widgets={

            "task_name":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"})

        }
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))