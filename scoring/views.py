from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import csv
# Create your views here.
class HomeListView(ListView):
    model = Judge
    template_name = 'home.html'

def home(request):
    return render(request, 'home.html')
    #return render(ListView, 'home.html')

    #def import_db(request):
    #    f = open('Open Scoring UNH Ver09.csv', 'r')
    #    for line in f:
    #        line = line.split(',')
    #        tmp = Judge.object.create()
    #        tmp.judge_id = line[]

def display_judges(request):
    items = Judge.objects.all()
    button = "judges"
    context = {
        'button' : button,
        'items' : items,
        #'name' : 
    }
    return render(request, 'home.html', context)

def display_projects(request):
    button = "projects"
    project_items = Project.objects.all()
    context = {
        'button' : button,
        'project_items' : project_items,
        #'name' : 
    }
    return render(request, 'home.html', context)

def display_judge_assignments(request):
    button = "judge_assignments"
    ja_items = Judge_Assignment.objects.all()
    context = {
        'button' : button,
        'ja_items' : ja_items,
        #'name' : 
    }
    return render(request, 'home.html', context)

def display_students(request):
    button = "students"
    student_items = Student.objects.all()
    context = {
        'button' : button,
        'student_items' : student_items,
        #'name' : 
    }
    return render(request, 'home.html', context)
