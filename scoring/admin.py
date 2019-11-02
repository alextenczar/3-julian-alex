from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from tablib import Dataset
from openpyxl import load_workbook
from string import ascii_uppercase

@admin.register(Judge, Project, Judge_Assignment, Student)
class ViewAdmin(ImportExportModelAdmin):
    wb = load_workbook(filename = 'Open Scoring UNH Ver09.xlsm')
    sheet = wb.active
    alphabet = ascii_uppercase
    #JUDGE
    judge_id = []
    name = []
    for C in alphabet[14:26]:
        j_id = sheet[str(C)+str(3)].value
        j_n = sheet[str(C)+str(4)].value
        if '-' in j_id and j_n:
            continue
        if j_id not in judge_id:
            judge_id.append(j_id)
        if j_n not in name:
            name.append(j_n)
    for C1 in alphabet[0:8]:
        for C2 in alphabet:
            j_id = sheet[str(C1)+str(C2)+str(3)].value
            j_n = sheet[str(C1)+str(C2)+str(4)].value
            if j_id is None:
                break
            if '-' in j_id and j_n:
                continue
            if j_id not in judge_id:
                judge_id.append(j_id)
            if j_n not in name:
                name.append(j_n)

    for s in range(5, 71):
    #PROJECT
        project_id = sheet['D'+str(s)].value
        description = sheet['L'+str(s)].value
        project_title = sheet['J'+str(s)].value
        project_category = sheet['K'+str(s)].value
        avg_score = sheet['LB'+str(s)].value
        rank = sheet['LC'+str(s)].value
        z_score = sheet['LD'+str(s)].value
        scaled_score = sheet['LH'+str(s)].value
        scaled_rank = sheet['LJ'+str(s)].value
        scaled_z = sheet['LI'+str(s)].value
        isef_score = sheet['LK'+str(s)].value
        isef_rank = sheet['LL'+str(s)].value

    #STUDENT
        ids = [sheet['E'+str(s)].value, sheet['F'+str(s)].value, sheet['G'+str(s)].value]
        school = sheet['H'+str(s)].value

    #JUDGE ASSIGNMENT
        judge_id_f = judge_id
        goal_score = 0
        plan_score = 0
        action_score = 0
        result_analysis_score = 0
        communication_score = 0
        raw_score = goal_score + plan_score + action_score + result_analysis_score + communication_score

    #SAVE STUDENT
        for id in ids:
            if id is not None:
                s = Student(id, school, project_id)
                # s.save()
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

class studentResource(resources.ModelResource):
    id = fields.Field(attribute='', column_name='E')
    school = fields.Field(attribute='', column_name='H')
    project_id = fields.Field(attribute='', column_name='D')
    """
