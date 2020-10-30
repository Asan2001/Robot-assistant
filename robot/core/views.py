import logging

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.models import Robot
from core.serializers import RobotSerializer

logger = logging.getLogger(__name__)


class RobotViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    def perform_create(self, serializer):
        return serializer.save(name=self.request.data['name'],
                               description=self.request.data['description'],
                               creator=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.filter(creator=self.request.user)
        return queryset

    @action(methods=['POST'], detail=True)
    def activate(self, request, pk):
        robot = Robot.objects.get(id=pk)
        robot.is_activated = True
        robot.save()
        return Response("Робот {} запущен".format(robot.name))

    @action(methods=['DELETE'], detail=True)
    def deactivate(self, request, pk):
        robot = Robot.objects.get(id=pk)
        robot.is_activated = False
        robot.save()
        return Response("Робот {} приостановлен".format(robot.name))
