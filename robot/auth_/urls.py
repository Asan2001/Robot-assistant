from rest_framework import routers

from auth_.views import MainUserViewSet

router = routers.DefaultRouter()
router.register(r'users', MainUserViewSet, base_name='auth_')

urlpatterns = router.urls
