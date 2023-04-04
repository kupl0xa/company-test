from django.db.models import Sum
from rest_framework import serializers

from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Employee"""

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeByDeptSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    employee = EmployeeSerializer(read_only=True, many=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'director', 'employee')


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Department"""
    director = serializers.StringRelatedField()
    employees_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'director', 'employees_count', 'total_salary')

    @staticmethod
    def get_employees_count(obj):
        return obj.employee.count()

    @staticmethod
    def get_total_salary(obj):
        return obj.employee.aggregate(Sum('salary'))['salary__sum']
