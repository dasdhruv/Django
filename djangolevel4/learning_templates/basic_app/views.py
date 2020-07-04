from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello I am from views module','number':100}
    return render(request, 'basic_app/index.html', context_dict)


def other(request):
    context_dict = {'text':'Hello I am from other class from the view.py script'}
    return render(request, 'basic_app/other.html', context_dict)

def relative(request):
    return render(request, 'basic_app/relative_url.html')
