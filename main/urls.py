from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments_list, name='departments_list'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    path('programs/', views.specialties_list, name='specialties_list'),
    path('programs/<int:program_id>/', views.program_detail, name='program_detail'),
    path('lecturers/', views.lecturers_list, name='lecturers_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
