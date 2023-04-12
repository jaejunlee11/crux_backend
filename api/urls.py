from django.urls import path, include
from .views import API

urlpatterns = [
    path("api/", API)
]