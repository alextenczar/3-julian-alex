from scoring.models import Judge
from string import ascii_uppercase

def import_judge(sheet):
    alphabet = ascii_uppercase
    #JUDGE
    judge_id = []
    name = []
    for C in alphabet[13:26]:
        j_id = sheet[str(C)+str(4)].value
        j_n = sheet[str(C)+str(3)].value
        if '-' in j_id and j_n:
            continue
        if j_id not in judge_id:
            judge_id.append(j_id)
        if j_n not in name:
            name.append(j_n)
    for C1 in alphabet[0:8]:
        for C2 in alphabet:
            j_id = sheet[str(C1)+str(C2)+str(4)].value
            j_n = sheet[str(C1)+str(C2)+str(3)].value
            if j_id is None:
                break
            if '-' in j_id and j_n:
                continue
            if j_id not in judge_id:
                judge_id.append(j_id)
            if j_n not in name:
                name.append(j_n)

    #SAVE JUDGE
    for j_id, j_n in zip(judge_id, name):
        j = Judge(j_id, j_n)
        j.save()

