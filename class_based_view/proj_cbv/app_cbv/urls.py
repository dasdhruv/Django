from django.urls import path, re_path
from app_cbv import views
#from django.contrib import admin

app_name = 'app_cbv'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='view_list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='school_details'),
]
