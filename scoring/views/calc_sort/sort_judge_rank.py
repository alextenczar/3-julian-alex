from scoring.models import Judge, Judge_Assignment

def sort_judge_rank():
    judges = list(Judge.objects.all())
    for judge in judges:
        jas = list(Judge_Assignment.objects.filter(judge_id = judge.judge_id).order_by('-raw_score'))
        for index in range(len(jas)):
            if jas[index].raw_score is None:
                continue
            jas[index].rank = (1-(1/(len(jas)-1))*index)
            if index > 0 and (jas[index].raw_score == jas[index-1].raw_score):
                jas[index].rank = jas[index-1].rank
            jas[index].save()