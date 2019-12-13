from scoring.models import Project

def sort_category_rank():
    projects = list(Project.objects.all().order_by('project_category', '-isef_score'))
    rank = 1
    for index in range(len(projects)):
        if index >= 0 and projects[index].project_category != projects[index-1].project_category:
            rank = 1
        projects[index].category_rank = rank
        if projects[index].isef_score is not None:
            if index > 0 and projects[index].isef_score == projects[index-1].isef_score:
                if projects[index].project_category == projects[index-1].project_category:
                    projects[index].category_rank = projects[index-1].category_rank
            rank = rank + 1
            projects[index].save()
