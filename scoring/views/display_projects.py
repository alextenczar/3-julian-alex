from scoring.models import Project
from django.shortcuts import render

def display_projects(request):
    button = "projects"
    project_items = Project.objects.all()
    context = {
        'button' : button,
        'project_items' : project_items,
        #'name' :
    }
    return render(request, 'home.html', context)

