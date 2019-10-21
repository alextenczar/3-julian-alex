from django.urls import path
from .views import *
#from .views import HomeListView

urlpatterns = [

    #path('', HomeListView.as_view(), name='home'),
    path('', home, name='home'),
    path('display_judges/', display_judges, name='display_judges'),
    path('display_projects/', display_projects, name='display_projects'),
    path('display_judge_assignments/', display_judge_assignments, name='display_judge_assignments'),
    path('display_students/', display_students, name='display_students'),
]
