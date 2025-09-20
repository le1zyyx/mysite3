from django.shortcuts import render, redirect

def index(request):
    data = {'title': 'Homepage'}
    return render(request, 'main/index.html', data)


def departments(request):
    return render(request, 'main/departments.html')

def specialties(request):
    return render(request, 'main/specialties.html')