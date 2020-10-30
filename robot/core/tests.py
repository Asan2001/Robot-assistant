from django.test import TestCase, RequestFactory
from core.models import Robot
from auth_.models import MainUser
from core.views import RobotViewSet


class RobotTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        user = MainUser.objects.create(first_name='test', last_name='test', username='test')
        self.robot = Robot.objects.create(name="robot1", description="robot", creator=user)
        self.pk = self.robot.id

    def test_robot_activate(self):
        request = self.factory.post('/robots/' + str(self.pk) + '/activate/')
        response = RobotViewSet.activate(self, request, self.pk)
        self.assertEqual(response.data, 'Робот {} запущен'.format(self.robot.name))

    def test_robot_deactivate(self):
        request = self.factory.delete('/robots/' + str(self.pk) + '/deactivate/')
        response = RobotViewSet.deactivate(self, request, self.pk)
        self.assertEqual(response.data, 'Робот {} приостановлен'.format(self.robot.name))
