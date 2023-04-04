from django.contrib import admin

from .models import Department, Employee


class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['last_name']
    list_filter = ['last_name']


admin.site.register(Department)
admin.site.register(Employee)
