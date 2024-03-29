from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from shahid_aleali.users.api.views import GroupViewSet, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)


app_name = "api"
urlpatterns = router.urls
