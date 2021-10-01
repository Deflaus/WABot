from rest_framework.routers import SimpleRouter
from .views import Bot


router = SimpleRouter()
router.register("", Bot, basename="bot")
urlpatterns = router.urls
