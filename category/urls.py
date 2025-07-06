from rest_framework.routers import DefaultRouter
from .views import CategoryPriceViewSet

router = DefaultRouter()
router.register(r'categories', CategoryPriceViewSet)

urlpatterns = router.urls
