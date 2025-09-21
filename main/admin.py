from django.contrib import admin
from .models import Department, Program, Lecturer, HomePageContent

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'coordinator_name')
    search_fields = ('name', 'code', 'coordinator_name')
    list_filter = ('department',)

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'position', 'degree')

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title',)
