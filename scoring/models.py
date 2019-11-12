from django.db import models

# Create your models here.
class Judge(models.Model):
    judge_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=10)

class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=6)
    description = models.CharField(max_length=1000)
    project_title = models.CharField(max_length=500)
    project_category = models.CharField(max_length=100)
    avg_score = models.FloatField(null=True)
    rank = models.IntegerField(null=True)
    z_score = models.FloatField(null=True)
    scaled_score = models.FloatField(null=True)
    scaled_rank = models.FloatField(null=True)
    scaled_z = models.FloatField(null=True)
    isef_score = models.FloatField(null=True)
    isef_rank = models.IntegerField(null=True)

class Student(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    #first_name = models.CharField()
    #last_name = models.CharField()
    school = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project, to_field='project_id', on_delete=models.CASCADE)

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
