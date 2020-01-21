from django.urls import path
from departments.api.views import DepartmentViewSet


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'departments', DepartmentViewSet, base_name='department')


# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
