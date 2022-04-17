from urllib import request
from django import forms
from django.http import HttpResponse
from ast import Pass
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.contrib.auth.views import LoginView,LogoutView
from .models import Contact, Task,TodoListItem 
from django.contrib import messages
from datetime import datetime
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .forms import TaskForm
# from django.contrib.auth import authenticate , login as loginUser
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import login,authenticate,logout

# Email ............................................

from django.conf import settings
from django.core.mail import send_mail, EmailMessage


# Create your views here.
class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url = "/user/userlogin/"
    # success_message = "%(name)s was created successfully"
  
    def form_valid(self, forms):
        user = forms.save()
        user.set_password(user.password) 
        user.save()  
        return super().form_valid(forms)

    def get_success_message(self,cleaned_data):
        username = cleaned_data["username"]
        return username + " - User created successfully..!!"

class UserLoginView(LoginView):
    template_name = 'userportal/login.html'
    success_url = "userportal/home/"


def index(request):
    return render(request, 'userportal/index.html')

def Homepage(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     form = TaskForm()
    #     todos = Task.objects.filter(user = user).order_by('priority')
    #     return render(request , 'userportal/homepage.html' , context={'form' : form , 'todos' : todos})
    return render(request,'userportal/homepage.html')  

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'userportal/contactus.html')

def Logout(request):
    return render(request, 'userportal/index.html')

# @login_required(login_url='user/userlogin/')
class AddTask(CreateView):
    model = Task
    form_class =TaskForm

    # fields = ['task_name','task_description','priority','status','Date']
    template_name = 'userportal/add_task.html'
    success_url = '/user/view'
    
        
        



# @login_required(login_url='user/userlogin/')
class ViewTask(ListView):
    model = Task
    tasks = model.objects.order_by('priority')
    context_object_name = 'tasks'
    template_name = 'userportal/view_task.html'
    redirect_field_name = '/user/userlogin/'

class DetailTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'userportal/detail_task.html'

class DeleteTask(DeleteView):
    model = Task
    template_name = "userportal/delete_task.html"
    success_url = "/user/view"

class UpdateTask(UpdateView):
    model = Task
    fields = ['task_name','task_description','Date']
    template_name = "userportal/update_task.html"
    success_url = "/user/view"

#  STATUS CHANGE
def change_task(request , id  , status):
    tasks = Task.objects.get(pk = id)
    tasks.status = status
    tasks.save()
    return redirect('/user/view')


# Email

def sendmail(request):
    subject = 'welcome'
    message = "greeting\nHi user! \nWelcome to Prioritizer! Thanks so much for joining us. You/’re on your way to super-productivity and beyond! \n[who we are; our mission/ what we help you do; how it works] \nPrioritizer is a task management app that helps you focus on the important things in life by only allowing you to add 3 items a day. Set and track daily, weekly, and monthly priorities — and get the stuff that matters done"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [form.username]
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse('mail sent')




