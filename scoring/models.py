from django.db import models
import csv

# Create your models here.
class Judge(models.Model):
    judge_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=10)

class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=6)
    description = models.CharField(max_length=1000)
    project_title = models.CharField(max_length=500)
    project_category = models.CharField(max_length=100)
    avg_score = models.FloatField()
    rank = models.IntegerField()
    z_score = models.FloatField()
    scaled_score = models.FloatField()
    scaled_rank = models.FloatField()
    scaled_z = models.FloatField()
    isef_score = models.FloatField()
    isef_rank = models.IntegerField()

class Student(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    #first_name = models.CharField()
    #last_name = models.CharField()
    school = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)

class Judge_Assignment(models.Model):
    judge_id_f = models.ForeignKey(Judge, on_delete=models.PROTECT)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    goal_score = models.IntegerField()
    plan_score = models.IntegerField()
    action_score = models.IntegerField()
    result_analysis_score = models.IntegerField()
    communication_score = models.IntegerField()
    raw_score = models.IntegerField()
