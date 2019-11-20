from scoring.views import Judge_Assignment

def import_judge_assignment(sheet):
    #JUDGE ASSIGNMENT
    goal_score = 0
    plan_score = 0
    action_score = 0
    result_analysis_score = 0
    communication_score = 0
    # raw_score = goal_score + plan_score + action_score + result_analysis_score + communication_score

    #SAVE JUDGE_ASSIGNMENT
    id = 0
    for row in sheet.iter_rows(min_row=5, min_col=13, max_row=71, max_col=220):
        for cell in row:
            if isinstance(cell.value,int):
                id = id + 1
                j_id = sheet.cell(row = 4, column = cell.column).value
                if '-' in j_id:
                    continue
                p_id = sheet.cell(row = cell.row, column = 4).value
                raw_score = cell.value
                ja = Judge_Assignment(id, j_id, p_id, goal_score, plan_score, action_score, result_analysis_score, communication_score, raw_score)
                ja.save()

