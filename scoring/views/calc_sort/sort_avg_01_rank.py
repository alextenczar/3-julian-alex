from scoring.models import Project

def sort_avg_01_rank():
    projects = list(Project.objects.all().order_by('-avg_01'))
    for index in range(len(projects)):
        if projects[index].avg_01 is None:
            continue
        projects[index].avg_01_rank = index+1
        if projects[index].avg_01 == projects[index-1].avg_01:
            projects[index].avg_01_rank = projects[index-1].avg_01_rank
        projects[index].save()