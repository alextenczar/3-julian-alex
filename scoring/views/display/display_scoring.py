from django.shortcuts import render, get_object_or_404
from scoring.models import Judge_Assignment# Project, Judge
from scoring.forms.scoring_form import ScoringForm

def add_score(request):
    if request.method == 'POST':
        form = ScoringForm(request.POST)
        if form.is_valid():
            judge_assignment = form.save()
    else:
        form = ScoringForm()
    return render(request, 'scoring.html', {'form':form})

# def edit_score(request):
#     num = list(Judge_Assignment.objects.all()).size()
#     ja = Judge_Assignment.objects.create()
#     form = ScoringForm(request.POST or None, instance = ja)
#     if form.is_valid():
#         form.save()
#     return render(request, 'scoring.html', {'form':form})

# def display_scoring(request):
#     judges = Judge.objects.all()
#     projects = Project.objects.all()
#     button = "judges"
#     context = {
#         'button' : button,
#         'judges' : judges,
#         'projects' : projects,
#         #'name' :
#     }
#     return render(request, 'scoring.html', context)
