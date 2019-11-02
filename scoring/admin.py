from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields

@admin.register(Judge, Project, Judge_Assignment, Student)
class ViewAdmin(ImportExportModelAdmin):
    pass


""" class judgeResource(resources.ModelResource):
    judge_id = fields.Field(attribute='judge_id', column_name='tbd')
    name = fields.Field(attribute='name', column_name='tbd')


class projectResource(resources.ModelResource):
    project_id = fields.Field(attribute='project_id', column_name='reg_number_short')
    description = fields.Field(attribute='description', column_name='project-description')
    project_title = fields.Field(attribute='', column_name='')
    project_category = fields.Field(attribute='', column_name='')
    avg_score = fields.Field(attribute='', column_name='')
    rank =  fields.Field(attribute='', column_name='')
    z_score = fields.Field(attribute='', column_name='')
    scaled_score = fields.Field(attribute='', column_name='')
    scaled_rank = fields.Field(attribute='', column_name='')
    scaled_z = fields.Field(attribute='', column_name='')
    isef_score = fields.Field(attribute='', column_name='')

class jaResource(resources.ModelResource):
    judge_id_f = fields.Field(attribute='', column_name='')
    project_id =fields.Field(attribute='', column_name='')
    goal_score = fields.Field(attribute='', column_name='')
    plan_score = fields.Field(attribute='', column_name='')
    action_score = fields.Field(attribute='', column_name='')
    result_analysis_score = fields.Field(attribute='', column_name='')
    communication_score = fields.Field(attribute='', column_name='')
    raw_score = fields.Field(attribute='', column_name='')
    """
'''
class studentResource(resources.ModelResource):
    id = fields.Field(attribute='', column_name='E')
    school = fields.Field(attribute='', column_name='H')
    project_id = fields.Field(attribute='', column_name='D')'''
