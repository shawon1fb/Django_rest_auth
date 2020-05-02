from django.contrib import admin
from django.urls import path
from .views import StatusList

urlpatterns = [
    path("status", StatusList.as_view())
]
