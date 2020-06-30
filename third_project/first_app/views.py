from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Users
def index(request):
    my_dict = {'insert_me':"Text is inserted from view"}
    return render(request,'first_app_template/index.html', context=my_dict)

def users(request):
    users = Users.objects.all()
    my_dict = {'insert_me':users}
    return render(request,'first_app_template/users.html', context=my_dict)
