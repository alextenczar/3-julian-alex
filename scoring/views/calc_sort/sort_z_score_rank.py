from scoring.models import Project

def sort_z_score_rank():
    rank = 1
    projects = list(Project.objects.all().order_by('-z_score'))
    for index in range(len(projects)):
        if projects[index].z_score is not None:
            projects[index].z_score_rank = rank
            rank = rank + 1
            if index > 0 and projects[index].z_score == projects[index-1].z_score:
                projects[index].z_score_rank = projects[index-1].z_score_rank
            projects[index].save()
