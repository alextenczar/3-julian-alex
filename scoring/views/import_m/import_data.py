from openpyxl import load_workbook
from scoring.views.import_m.import_judge import import_judge
from scoring.views.import_m.import_student import import_student
from scoring.views.import_m.import_project import import_project
from scoring.views.import_m.import_judge_assignment import import_judge_assignment

def import_data(request):
    wb = load_workbook(filename = request, data_only=True)
    sheet = wb.active
    import_judge(sheet)
    import_project(sheet)
    import_student(sheet)
    import_judge_assignment(sheet)