from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord
def index(request):
    date_in_asc = AccessRecord.objects.order_by('date')
    my_dict = {'insert_me':date_in_asc}
    return render(request,'first_app_template/index.html', context=my_dict)
