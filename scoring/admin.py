from django.contrib import admin

# Register your models here.
@admin.register(Judge, Project, Judge_Assignment, Student):
class ViewAdmin(admin.ModelAdmin):
    pass
