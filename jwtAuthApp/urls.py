from django.urls import path

from jwtAuthApp.views import JwtAuthApp, LoginWithoutSerializer, RegisterWithoutSerializer

urlpatterns = [
    path("", JwtAuthApp.as_view()),
    path("login", LoginWithoutSerializer.as_view()),
    path("register", RegisterWithoutSerializer.as_view()),
]
