from scoring.models import Judge_Assignment
from statistics import mean, stdev

def cal_z_score():
    jas = list(Judge_Assignment.objects.all())
    for ja in jas:
        jas_projects = list(Judge_Assignment.objects.filter(judge_id = ja.judge_id))
        all_judge_scores = []
        for jas_project in jas_projects:
            all_judge_scores.append(jas_project.raw_score)
        if not all_judge_scores:
            continue
        ja.z_score = (ja.raw_score - mean(all_judge_scores))/stdev(all_judge_scores)
        ja.save()