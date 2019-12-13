from django.db import models

class Judge(models.Model):
    judge_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=10)