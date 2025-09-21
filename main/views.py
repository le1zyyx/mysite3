from django.shortcuts import render, get_object_or_404
from .models import Department, Program

def index(request):
    department = Department.objects.first()
    contacts = {
        'phone': '(044) 425 60 64',
        'address': 'вул. Г. Сковороди 2, 1 корпус НаУКМА, кім. 315',
        'email': 'fin@ukma.edu.ua'
    }
    return render(request, 'main/index.html', {'department': department, 'contacts': contacts})

def departments(request):
    departments = Department.objects.all()  # Отримай всі кафедри
    return render(request, 'main/departments.html', {'departments': departments})

def specialties(request):
    programs = Program.objects.all()
    return render(request, 'main/specialties.html', {'programs': programs})

# Додай детальні функції
def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    teachers = department.teachers.all() if hasattr(department, 'teachers') else []
    programs = department.programs.all() if hasattr(department, 'programs') else []
    return render(request, 'main/department_detail.html', {
        'department': department,
        'teachers': teachers,
        'programs': programs
    })

def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render(request, 'main/program_detail.html', {'program': program})
