from scoring.models import Project

def cal_scaled_score():
    projects = list(Project.objects.all())
    for index in range(len(projects)):
        min = list(Project.objects.all().order_by('avg_score'))[index].avg_score
        if min is not None:
            break
    for index in range(len(projects)):
        max = list(Project.objects.all().order_by('-avg_score'))[index].avg_score
        if max is not None:
            break
    rangevalue = max - min
    for project in projects:
        if project.avg_score is None:
            continue
        project.scaled_score = ((project.avg_score - min)/rangevalue)*25 + 25
        project.save()
