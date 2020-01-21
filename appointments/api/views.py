from rest_framework import viewsets
from .serializers import AppointmentSerializer, ClassificationSerializer, InviteSerializer, PurposeSerializer, VisitorRegistrationSerializer

from appointments.models import Appointment, Classification, Invite, Purpose, VisitorRegistration


class VisitorRegistrationViewSet(viewsets.ModelViewSet):

    serializer_class = VisitorRegistrationSerializer
    queryset = VisitorRegistration.objects.all()


class PurposeViewSet(viewsets.ModelViewSet):

    serializer_class = PurposeSerializer
    queryset = Purpose.objects.all()


class InviteViewSet(viewsets.ModelViewSet):

    serializer_class = InviteSerializer
    queryset = Invite.objects.all()


class ClassificationViewSet(viewsets.ModelViewSet):

    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()


class AppointmentViewSet(viewsets.ModelViewSet):

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
