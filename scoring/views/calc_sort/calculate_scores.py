from scoring.views.calc_sort.cal_raw_score import cal_raw_score
from scoring.views.calc_sort.cal_average_score import cal_average_score
from scoring.views.calc_sort.sort_rank import sort_rank
from scoring.views.calc_sort.cal_z_score import cal_z_score
from scoring.views.calc_sort.sort_judge_rank import sort_judge_rank
from scoring.views.calc_sort.cal_avg_z_score import cal_avg_z_score
from scoring.views.calc_sort.sort_z_score_rank import sort_z_score_rank
from scoring.views.calc_sort.cal_avg_01 import cal_avg_01
from scoring.views.calc_sort.sort_avg_01_rank import sort_avg_01_rank
from scoring.views.calc_sort.cal_scaled_score import cal_scaled_score
from scoring.views.calc_sort.cal_scaled_score import cal_scaled_score
from scoring.views.calc_sort.cal_avg_z_score import cal_avg_z_score
from scoring.views.calc_sort.cal_scaled_rank import cal_scaled_rank
from scoring.views.calc_sort.cal_scaled_z_score import cal_scaled_z_score
from scoring.views.calc_sort.cal_isef_score import cal_isef_score
from scoring.views.calc_sort.sort_isef_rank import sort_isef_rank
from scoring.views.calc_sort.sort_category_rank import sort_category_rank
from django.shortcuts import render



def calculate_scores(request):
    cal_raw_score()
    cal_average_score()
    sort_rank()
    cal_z_score()
    sort_judge_rank()
    cal_avg_z_score()
    sort_z_score_rank()
    cal_avg_01()
    sort_avg_01_rank()
    cal_scaled_score()
    cal_scaled_z_score()
    cal_scaled_rank()
    cal_isef_score()
    sort_isef_rank()
    sort_category_rank()
    return render(request, 'home.html')
