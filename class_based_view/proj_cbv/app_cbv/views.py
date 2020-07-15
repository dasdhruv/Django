from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# Create your views here.

# Function based views defined
def index(request):
    return render(request, 'app_cbv/index.html')

# class based views defined
class CbvExample(View):
    # get is a function provided by django.views.generic module
    def get(this, request):
        return HttpResponse("Class based view is called:")

# Template based views defined
class TbvExample(TemplateView):
    template_name = 'app_cbv/index.html'

    def get_context_data(this, **kwargs):
        data = super().get_context_data(**kwargs)
        data['val_1'] = "My Value is One"
        data['val_2'] = "My Value is Two"
        return data

class SchoolListView(ListView):
    # the returned school names from the database can be kept in the variable(schools i have chosen the variable name) of your choice by saying
    context_object_name = 'schools'
    model = models.School
    template_name = 'app_cbv/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'app_cbv/school_details.html'
