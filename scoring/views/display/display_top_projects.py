from scoring.models import Project
from django.shortcuts import render

def display_top_projects(request):
    button = "top_projects"
    top_all = list(Project.objects.order_by('fair_rank').exclude(fair_rank__isnull=True)[:5])
    # for p in list(top_all):
    #     print(p.project_title)
    projects = list(Project.objects.all())
    categories = []
    for project in projects:
        if not project.project_category in categories:
            categories.append(project.project_category)

    top_all_categories = []

    for category in categories:
        top_in_category = Project.objects.filter(project_category=category).order_by('category_rank')[:5]
        top_all_categories.append(top_in_category)
        # for t in top_in_category:
        #     print(t.category_rank)
    # for t in top:
    #     for o in t:
    #         print(o.category_rank)

    context = {
        'button' : button,
        'top_all' : top_all,
        'top_all_categories' : top_all_categories,
        #'name' :
    }
    return render(request, 'home.html', context)
