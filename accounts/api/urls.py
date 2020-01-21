from django.urls import path
from accounts.api.views import UserViewSet, StaffViewSet, StatusViewSet, PositionViewSet


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'staff', StaffViewSet, base_name='staff')
router.register(r'position', PositionViewSet, base_name='position')
router.register(r'status', StatusViewSet, base_name='status')


# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
