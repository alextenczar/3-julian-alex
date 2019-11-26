from scoring.models import Project

def cal_isef_score():
    projects = list(Project.objects.all())
    for project in projects:
        if project.scaled_score is None or project.scaled_rank is None or project.scaled_z is None:
            continue
        project.isef_score = (project.scaled_score + project.scaled_rank + project.scaled_z) - 50
        project.save()