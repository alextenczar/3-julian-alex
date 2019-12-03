from scoring.models import Project

def sort_rank():
    rank = 1
    projects = list(Project.objects.all().order_by('-avg_score'))
    for index in range(len(projects)):
        if isinstance(projects[index].avg_score,float):
            projects[index].rank = rank
            rank = rank + 1
            if index > 0 and projects[index].avg_score == projects[index-1].avg_score:
                projects[index].rank = projects[index-1].rank
            projects[index].save()
