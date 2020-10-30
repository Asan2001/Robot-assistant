from rest_framework import serializers

from auth_.serializers import MainUserSerializer
from core.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'
        read_only_fields = ('creator',)
