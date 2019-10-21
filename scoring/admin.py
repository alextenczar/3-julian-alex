from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Judge, Project, Judge_Assignment, Student)
class ViewAdmin(admin.ModelAdmin):
    pass
