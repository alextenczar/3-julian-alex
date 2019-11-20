from scoring.models import Student
from django.shortcuts import render

def display_students(request):
    button = "students"
    student_items = Student.objects.all()
    context = {
        'button' : button,
        'student_items' : student_items,
        #'name' :
    }
    return render(request, 'home.html', context)

