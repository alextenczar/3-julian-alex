from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .views import *

@admin.register(Judge, Project, Judge_Assignment, Student)
class ViewAdmin(ImportExportModelAdmin):
    pass
