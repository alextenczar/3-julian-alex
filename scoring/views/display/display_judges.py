from django.shortcuts import render
from scoring.models import Judge

def display_judges(request):
    items = Judge.objects.all()
    button = "judges"
    context = {
        'button' : button,
        'items' : items,
        #'name' :
    }
    return render(request, 'home.html', context)
