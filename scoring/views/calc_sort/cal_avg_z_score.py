from scoring.models import Judge_Assignment, Project
from statistics import mean

def cal_avg_z_score():
    projects = list(Project.objects.all())
    for project in projects:
        jas_z_score = list(Judge_Assignment.objects.filter(project_id = project.project_id).values_list('z_score', flat=True))
        if not jas_z_score:
            continue
        project.z_score = mean(jas_z_score)
        project.save()