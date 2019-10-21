from django.shortcuts import render
from django.views.generic import ListView
from .models import Judge
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

#def display_judges(request):
 #   judge