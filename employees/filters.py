from django_filters import rest_framework

from .models import Employee


class EmployeeFilter(rest_framework.FilterSet):
    department = rest_framework.NumberFilter()
    last_name = rest_framework.CharFilter(
        field_name='last_name',
        lookup_expr='exact'
    )

    class Meta:
        model = Employee
        fields = ('last_name', 'department')
