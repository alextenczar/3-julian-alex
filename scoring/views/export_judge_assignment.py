import csv
from scoring.models import Judge_Assignment
from django.http import HttpResponse

def export_jugde_assignment(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="judge_assignments.csv"'

    writer = csv.writer(response)
    writer.writerow(['Judge ID', 'Project ID', 'Raw Score'])

    jas = Judge_Assignment.objects.all().values_list('judge_id', 'project_id', 'raw_score')
    for ja in jas:
        writer.writerow(list(ja))

    return response
