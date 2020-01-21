from appointments.api.views import AppointmentViewSet, VisitorRegistrationViewSet, ClassificationViewSet, PurposeViewSet, InviteViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'appointments', AppointmentViewSet, base_name='appointments')
router.register(r'classifications', ClassificationViewSet,
                base_name='classifications')
router.register(r'visitor-registration',
                VisitorRegistrationViewSet, base_name='visitor-registration')
router.register(r'purpose', PurposeViewSet, base_name='purpose')
router.register(r'invite', InviteViewSet, base_name='invite')


urlpatterns = router.urls
