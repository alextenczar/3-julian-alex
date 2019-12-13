from scoring.models import Project

def sort_avg_01_rank():
    rank = 1
    projects = list(Project.objects.all().order_by('-avg_01'))
    for index in range(len(projects)):
        if projects[index].avg_01 is not None:
            projects[index].avg_01_rank = rank
            rank = rank + 1
            if index > 0 and projects[index].avg_01 == projects[index-1].avg_01:
                projects[index].avg_01_rank = projects[index-1].avg_01_rank
            projects[index].save()
