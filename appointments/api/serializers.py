from appointments.models import Appointment, Classification, Invite, Purpose, VisitorRegistration


from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ("__all__")


class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = ("__all__")


class PurposeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purpose
        fields = ("__all__")


class InviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invite
        fields = ("__all__")


class VisitorRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitorRegistration
        fields = ("__all__")
