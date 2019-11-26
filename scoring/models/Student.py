from django.db import models
from scoring.models.Project import Project

class Student(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    #first_name = models.CharField()
    #last_name = models.CharField()
    school = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project, to_field='project_id', on_delete=models.CASCADE)