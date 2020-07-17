from django.urls import path
from app_cbv import views
#from django.contrib import admin

app_name = 'app_cbv'


"""
http://127.0.0.1:8000/app_cbv/create will render below the view SchoolCreateView
"""
urlpatterns = [
    path('',views.SchoolListView.as_view(),name='view_list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='school_details'),
    path('create/',views.SchoolCreateView.as_view(),name='school_create'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='school_update'),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name='school_delete')
]
