from scoring.models import Judge_Assignment
from django.shortcuts import render

def display_judge_assignments(request):
    button = "judge_assignments"
    ja_items = Judge_Assignment.objects.all()
    context = {
        'button' : button,
        'ja_items' : ja_items,
        #'name' :
    }
    return render(request, 'home.html', context)

