from scoring.models import Project

def sort_rank():
    projects = list(Project.objects.all().order_by('-avg_score'))
    for i in range(len(projects)):
        projects[i].rank = i+1
        if not isinstance(projects[i].avg_score,float):
            projects[i].rank = None
            continue
        if i == 0:
            projects[i].rank = i+1
            continue
        if projects[i].avg_score == projects[i-1].avg_score:
            projects[i].rank = projects[i-1].rank
            continue
        projects[i].save()