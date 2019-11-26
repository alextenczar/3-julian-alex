from scoring.models import Judge_Assignment, Project

def cal_average_score():
    done_list = []
    jas = list(Judge_Assignment.objects.all())
    for ja in jas:
        if ja.project_id not in done_list:
            score = 0
            done_list.append(ja.project_id)
            project = Judge_Assignment.objects.filter(project_id = ja.project_id.project_id)
            for p in project:
                score = score + p.raw_score
            avg_score = score / len(list(project))
            if score == 0:
                continue
            project = Project.objects.get(project_id = ja.project_id.project_id)
            project.avg_score = avg_score
            project.save()