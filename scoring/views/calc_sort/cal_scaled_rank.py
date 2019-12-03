
from scoring.models import Project

def cal_scaled_rank():
    projects = list(Project.objects.all())
    for index in range(len(projects)):
        min = list(Project.objects.all().order_by('avg_01'))[index].avg_01
        if min is not None:
            break
    for index in range(len(projects)):
        max = list(Project.objects.all().order_by('-avg_01'))[index].avg_01
        if max is not None:
            break
    rangevalue = max - min
    for project in projects:
        if project.avg_01_rank is None:
            continue
        project.scaled_rank = ((project.avg_01 - min)/rangevalue)*25 + 25
        project.save()
