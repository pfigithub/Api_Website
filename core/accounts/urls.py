from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    path('api/v2/', include('allauth.urls')),
    path('api/v3/', include('djoser.urls')),
    path('api/v3', include('djoser.urls.authtoken')),
    path('api/v3', include('djoser.urls.jwt')),
]







