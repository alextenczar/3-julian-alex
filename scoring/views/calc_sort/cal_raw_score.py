from scoring.models import Judge_Assignment

def cal_raw_score():
    jas = list(Judge_Assignment.objects.all())
    for ja in jas:
        if ja.goal_score != 0 and ja.plan_score != 0 and ja.action_score != 0 and ja.result_analysis_score != 0 and ja.communication_score != 0:
            ja.raw_score = ja.goal_score + ja.plan_score + ja.action_score + ja.result_analysis_score + ja.communication_score
            ja.save()
