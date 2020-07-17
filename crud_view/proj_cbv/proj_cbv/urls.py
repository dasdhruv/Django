"""proj_cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_cbv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # let us call the function based views
    # path('', views.index, name='home')
    # let us call the class based views
    # path('', views.CbvExample.as_view(), name='home')
    # let us call the template based views
    path('', views.TbvExample.as_view(), name='home'),
    path('app_cbv/', include('app_cbv.urls',namespace='app_cbv')),

]
