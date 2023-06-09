from django.db.models import Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from .filters import EmployeeFilter
from .models import Department, Employee
from .pagination import CustomPageNumberPagination
from .serializers import (DepartmentSerializer, EmployeeByDeptSerializer,
                          EmployeeSerializer)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter


class EmployeeByDeptViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.select_related(
        'director').prefetch_related('employee')
    serializer_class = EmployeeByDeptSerializer


class DepartmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.annotate(
        employees_count=Count('employee'),
        total_salary=Sum('employee__salary')
    ).select_related('director')
    serializer_class = DepartmentSerializer
