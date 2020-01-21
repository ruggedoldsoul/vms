from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from accounts.models import User, Title, Status, Staff, Position

from .serializers import UserSerializer, PositionSerializer, StaffSerializer, TitleSerializer, StatusSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class PositionViewSet(viewsets.ModelViewSet):

    serializer_class = PositionSerializer
    queryset = Position.objects.all()


class StatusViewSet(viewsets.ModelViewSet):

    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class StaffViewSet(viewsets.ModelViewSet):

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
