from rest_framework.routers import DefaultRouter

from .views import BoundaryViewSet

router = DefaultRouter()

router.register(
    prefix="api/v1/boundaries", basename="boundaries", viewset=BoundaryViewSet
)

urlpatterns = router.urls
