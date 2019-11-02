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

""" class All_Models(models.Model):
    judge_id = models.ForeignKey(Judge, on_delete=models.PROTECT, related_name='judge_id')
    name = models.ForeignKey(Judge, on_delete=models.PROTECT, related_name='name')
    
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='project_id')
    description = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='description')
    project_title = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='project_title')
    project_category = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='project_category')
    avg_score = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='avg_score')
    rank = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='rank')
    z_score = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='z_score')
    scaled_score = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='scaled_score')
    scaled_rank = models.ForeignKey(Project, on_delete=models.PROTECT, related_name= 'scaled_rank')
    scaled_z = models.ForeignKey(Project, on_delete=models.PROTECT, related_name= 'scaled_z')
    isef_score = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='isef_score')
    isef_rank = models.ForeignKey(Project, on_delete=models.PROTECT,related_name='isef_rank')

    goal_score = models.ForeignKey(Judge_Assignment, on_delete=models.PROTECT, related_name='goal_score')
    plan_score = models.ForeignKey(Judge_Assignment, on_delete=models.PROTECT, related_name='plan_score')
    action_score = models.ForeignKey(Judge_Assignment, on_delete=models.PROTECT, related_name='action_score')
    result_analysis_score = models.ForeignKey(Judge_Assignment, on_delete=models.PROTECT, related_name='result_analysis_score')
    communication_score = models.ForeignKey(Judge_Assignment, on_delete=models.PROTECT, related_name='communication_score')
    raw_score = models.ForeignKey(Judge_Assignment, on_delete=models.PROTECT, related_name='raw_score')

    id_f = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='id_f')
    school = models.ForeignKey(Student, on_delete=models.PROTECT, related_name= 'school')
 """