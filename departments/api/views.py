from rest_framework import viewsets
from .serializers import DepartmentSerializer

from departments.models import Department


class DepartmentViewSet(viewsets.ModelViewSet):

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
