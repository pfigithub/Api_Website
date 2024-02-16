from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"


router = DefaultRouter()
router.register("test", views.TestView, basename="test")
# router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls
