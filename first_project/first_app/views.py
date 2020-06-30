from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    #return HttpResponse("hello_world")
    #return HttpResponse("<em>This is the index page</em>")
    return render(request,'first_app_template/image.html',)
# Create your views here.

def get_help(request):
    my_dict = {'insert_me':'I am from views.py'}
    return render(request,'first_app_template/help.html', context=my_dict)
