from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from openpyxl import load_workbook
from string import ascii_uppercase
from .convertStrToNum import float1, int1
from .views import *

@admin.register(Judge, Project, Judge_Assignment, Student)
class ViewAdmin(ImportExportModelAdmin):
    pass
