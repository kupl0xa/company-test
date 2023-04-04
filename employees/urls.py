from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DepartmentViewSet, EmployeeByDeptViewSet, EmployeeViewSet

app_name = 'api'

router = DefaultRouter()

router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)
router.register('employees_by_dept', EmployeeByDeptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
