from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    return render(request, 'basicapp/index.html')

def MyForm(request):
    f = forms.FormName()

    if request.method == 'POST':
        f = forms.FormName(request.POST)
        if f.is_valid():
            print("The name you entered::"+f.cleaned_data['Name'])
            print("The email you entered::"+f.cleaned_data['email'])
            print("The text you entered::"+f.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form':f})
