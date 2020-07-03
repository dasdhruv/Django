from django.urls import path
from appTwo import views
from django.contrib import admin

urlpatterns = [
    path('',views.users,name='users'), 
]
