from django.shortcuts import render
from scoring.views import import_data

def import_file(request):
    if request.method=='POST':
        file = request.FILES['document']
        import_data(file)
    return render(request, 'import.html')

