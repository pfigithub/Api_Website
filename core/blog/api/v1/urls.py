from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"


router = DefaultRouter()
router.register("post", views.PostView, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls
