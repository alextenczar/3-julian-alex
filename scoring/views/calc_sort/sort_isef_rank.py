from scoring.models import Project

def sort_isef_rank():
    projects = list(Project.objects.all().order_by('-isef_score'))
    for index in range(len(projects)):
        if projects[index].isef_score is None:
            continue
        projects[index].isef_rank = index+1
        if index > 0 and projects[index].isef_score == projects[index-1].isef_score:
            projects[index].isef_rank = projects[index-1].isef_rank
        projects[index].fair_rank = projects[index].isef_rank
        projects[index].save()

