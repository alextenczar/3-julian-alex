from scoring.models import Project
from scoring.convertStrToNum import float1, int1

def import_project(sheet):
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

    #SAVE PROJECT
        p = Project(project_id, description, project_title, project_category, float1(avg_score), int1(rank), float1(z_score), float1(scaled_score), float1(scaled_rank), float1(scaled_z), float1(isef_score), int1(isef_rank))
        p.save()

