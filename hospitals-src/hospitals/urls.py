from rest_framework.routers import DefaultRouter

from .views import HospitalViewSet

router = DefaultRouter()

router.register(
    prefix="api/v1/hospitals", basename="hospitals", viewset=HospitalViewSet
)

urlpatterns = router.urls
