from scoring.models import Student

def import_student(sheet):
    for s in range(5, 71):
    #STUDENT
        project_id = sheet['D'+str(s)].value
        ids = [sheet['E'+str(s)].value, sheet['F'+str(s)].value, sheet['G'+str(s)].value]
        school = sheet['H'+str(s)].value

    #SAVE STUDENT
        for id in ids:
            if id is not None:
                s = Student(id, school, project_id)
                s.save()

