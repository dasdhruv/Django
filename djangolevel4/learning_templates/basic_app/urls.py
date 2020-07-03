from django.urls import include, path
from . import views

# Set your app name to the global django app name so that Django can understand that your app name is basic_app
app_name = 'basic_app'

urlpatterns = [
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other_page'),
]
