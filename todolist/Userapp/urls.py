from django.contrib import admin
from django.urls import include, path
from .views import * 
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'user_urls'

urlpatterns = [
   
    path('userregistration/',BaseRegisterView.as_view(),name='userregistration'),
    path('userlogin/',UserLoginView.as_view(),name='userlogin'),
    path("index/",views.index),
    path('home/', views.Homepage,name='home'),
    path('contact/', views.contact,name='contact'),
    path("logout/",views.Logout,name="logout"),

    path('add/',AddTask.as_view(),name='add_task'),
    # path('add/',views.AddTask,name='add_task'),

    path('view/',ViewTask.as_view(),name='view_task'),
    # path('view/',views.ViewTask,name='view_task'),

    path('<int:pk>/detail/',DetailTask.as_view(),name='detail_task'),
    path('<int:pk>/delete/',DeleteTask.as_view(),name='delete_task'),
    path('<int:pk>/update/',UpdateTask.as_view(),name='update_task'),
#    path('view/', login_required(ViewTask.as_view(),login_url='/user/userlogin')),
    path('email/',views.sendmail,name='send_mail'),
   path('change-status/<int:id>/<str:status>', change_task ), 


]