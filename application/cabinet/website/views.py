from django.shortcuts import render
from .models import Staff

# Create your views here.


def index(request):
    staffs = Staff.objects.all()
    return render(request, 'website/index.html', {"staffs": staffs})
