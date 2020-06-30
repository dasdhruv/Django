from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.get_help, name='get_help'),
]
