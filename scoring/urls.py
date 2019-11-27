from django.urls import path
import scoring.views
from scoring.views import *
from scoring.views.remove_all_data import remove_all_data

#from .views import HomeListView

urlpatterns = [

    #path('', HomeListView.as_view(), name='home'),
     path('', display_projects, name='display_judges'),
    path('display_judges/', display_judges, name='display_judges'),
    path('display_projects/', display_projects, name='display_projects'),
    path('display_judge_assignments/', display_judge_assignments, name='display_judge_assignments'),
    path('display_students/', display_students, name='display_students'),
    path('import_file/', import_file, name='import_file'),
    path('export_judge_assignment/', export_judge_assignment, name='export_judge_assignment'),
    path('remove_all_data/', remove_all_data, name='remove_all_data'),
    path('calculate_scores/', calculate_scores, name='calculate_scores')
]
#test