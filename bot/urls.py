from rest_framework import routers
from .views import Bot


router = routers.DefaultRouter()
router.register(r"", Bot, basename="bot")
urlpatterns = router.urls