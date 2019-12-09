from django.db import models
from scoring.models.Judge import Judge
from scoring.models.Project import Project

class Judge_Assignment(models.Model):
    ja_id = models.IntegerField(primary_key=True, default='1')
    judge_id = models.ForeignKey(Judge, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    goal_score = models.IntegerField(null=True)
    plan_score = models.IntegerField(null=True)
    action_score = models.IntegerField(null=True)
    result_analysis_score = models.IntegerField(null=True)
    communication_score = models.IntegerField(null=True)
    raw_score = models.IntegerField(null=True)
    z_score = models.FloatField(null=True)
    rank = models.FloatField(null=True)

    def __str__(self):
        return self.ja_id
