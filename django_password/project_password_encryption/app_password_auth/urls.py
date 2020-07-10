from django.urls import path
from app_password_auth import views
from django.contrib import admin

app_name = 'app_password_auth'
urlpatterns = [
    path('',views.register,name='view_register'),
]
