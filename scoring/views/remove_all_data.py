from scoring.models import *
from django.shortcuts import render

def remove_all_data(request):
    Judge.objects.all().delete()
    Project.objects.all().delete()
    Student.objects.all().delete()
    Judge_Assignment.objects.all().delete()
    return render(request, 'home.html')


