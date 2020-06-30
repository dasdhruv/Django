from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.users, name='get_users'),
]
