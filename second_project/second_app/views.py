from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.
def index(request):
    webpages_list = User.objects.order_by('first_name')
    date_dict = {'access_records': webpages_list}
    return render(request, 'second_app/index.html', context=date_dict)
