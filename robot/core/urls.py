from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import RobotViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'robots', RobotViewSet, base_name='core')
urlpatterns += router.urls
