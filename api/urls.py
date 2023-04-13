from django.urls import path, include
from .views import *

from django.contrib import admin

# python3 manage.py runserver 0.0.0.0:8000 서버 실행

# 재준 : django 프로젝트 생성 api와 연결되는 url생성
# 재준 : db와 연결되는 api url생성
urlpatterns = [
    path("api/", API),
    # 숫자에 따라서 다른 값을 받고 싶은 경우 int:id로 path 정의 하기
    path("<int:id>",getDB),
    path("test/",getTest),
     path('postTest/', postTest, name="postMember"),
]

