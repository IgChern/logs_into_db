from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LogsViewSet

app_name = "log_app"

router = DefaultRouter()
router.register(r"logs", LogsViewSet, basename="logs")

urlpatterns = [
    path("", include(router.urls)),
]
