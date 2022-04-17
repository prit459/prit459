from django import forms
from django.contrib.auth.models import User
from .models import *
from .models import Task
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username', 'email','password','phone_number')

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ("username", "email", "password", "is_superuser", "is_staff", "is_active", "phone_number",)

CHOICES = (
        ("H", "Home"),
        ("W", "Work"),
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name' ,'task_description', 'status' , 'priority']


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        # my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)
        fields = ['task_name' ,'task_description', 'status' , 'priority','Date']
        widgets = {
            'Date': DateInput(),
        }