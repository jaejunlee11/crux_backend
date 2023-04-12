from django.urls import path, include
from .views import API
# 재준 : django 프로젝트 생성 api와 연결되는 uri생성
urlpatterns = [
    path("api/", API)
]