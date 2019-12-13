from scoring.models import Project

def cal_scaled_z_score():
    projects = list(Project.objects.all())
    for index in range(len(projects)):
        min = list(Project.objects.all().order_by('z_score'))[index].z_score
        if min is not None:
            break
    max = list(Project.objects.all().order_by('-z_score'))[0].z_score
    rangevalue = max - min
    for project in projects:
        if project.z_score is None:
            continue
        project.scaled_z = ((project.z_score - min)/rangevalue)*25 + 25
        project.save()

