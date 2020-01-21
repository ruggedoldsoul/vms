from accounts.models import User, Title, Status, Staff, Position
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("__all__")


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ("__all__")


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ("__all__")


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ("__all__")



class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Position
        fields=("__all__")
