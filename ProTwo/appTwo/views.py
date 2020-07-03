from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterNewUser
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    f = RegisterNewUser()

    if request.method == 'POST':
        f = RegisterNewUser(request.POST)

    if f.is_valid():
        f.save(commit=True)
        return render(request,'apptwo/index.html')

    return render(request, 'appTwo/users.html', {'form':f})
