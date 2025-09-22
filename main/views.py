from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Lecturer, HomePageContent

def index(request):
    homepage = HomePageContent.objects.first()
    contacts = {
        'phone': '(044) 425 60 64',
        'address': 'вул. Г. Сковороди 2, 1 корпус НаУКМА, кім. 315',
        'email': 'fin@ukma.edu.ua'
    }
    return render(request, 'main/index.html', {'homepage': homepage, 'contacts': contacts})

<<<<<<< HEAD
def departments_list(request):
    departments = Department.objects.all()
=======
def departments(request):
    departments = Department.objects.all() 
>>>>>>> 2674e7e98ce516c8dfc083ce720cbad698f76b82
    return render(request, 'main/departments.html', {'departments': departments})

def specialties_list(request):
    programs = Program.objects.all()
    return render(request, 'main/specialties.html', {'programs': programs})

<<<<<<< HEAD
def lecturers_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'main/lecturers.html', {'lecturers': lecturers})
=======
>>>>>>> 2674e7e98ce516c8dfc083ce720cbad698f76b82

def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    lecturers = department.lecturers.all()
    programs = department.programs.all()
    return render(request, 'main/department_detail.html', {
        'department': department,
        'lecturers': lecturers,
        'programs': programs,
    })

def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render(request, 'main/program_detail.html', {'program': program})
