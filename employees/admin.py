from django.contrib import admin

from .models import Department, Employee


@admin.register(Department)
class DepartmentModelAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'director')


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    ordering = ('last_name',)
    list_display = ('last_name', 'first_name', 'job_title', 'department')
    list_filter = ('department',)
    search_fields = ('last_name__startswith',)
