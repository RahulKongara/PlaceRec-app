from rest_framework.routers import DefaultRouter
from .views import LandmarkViewSet

router = DefaultRouter()
router.register(r"", LandmarkViewSet, basename="landmark")

urlpatterns = router.urls   
