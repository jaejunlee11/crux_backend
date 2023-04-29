from django.urls import path, include
from .views import *

from django.contrib import admin

# python3 manage.py runserver 0.0.0.0:8000 서버 실행

# 재준 : django 프로젝트 생성 api와 연결되는 url생성
# 재준 : db와 연결되는 api url생성
# 민재 : 동일한 작업 이후 작업부분에 맞춰 생성
# rest api 설계규칙과 일치하는지 확인 필요
'''
0. '/'는 계층 관계를 나타내는데 사용한다.
ex) GET: /users/2/orders

1. 마지막에는 '/' 사용하지 않는다.
ex) http://api.test.com/users/ (x) -> http://api.test.com/users

2. '_' 대신 '-'를 사용하고, 이 또한 최소한으로 한다.
ex) http://api.test.com/users/post_commnets (x) -> http://api.test.com/users/post-commnets

3. 소문자만 사용한다.
ex) http://api.test.com/users/postCommnets (x) -> http://api.test.com/users/post-commnets

4. 행위(method)는 URL에 포함하지 않는다.
ex) POST http://api.test.com/users/1/delete-post/1 (x) -> DELETE http://api.test.com/users/1/posts/1

5. 파일 확장자는 URI에 포함하지 않는다. 대신 accept header를 사용함.
ex) GET: http://restapi.exam.com/orders/2/Accept: image/jpg

6. 컨트롤 자원을 의미하는 URL에만 예외적으로 동사를 허용한다.
ex) http://api.test.com/posts/duplicating (x) -> http://api.test.com/posts/duplicate
'''

urlpatterns = [
    path("api/", API),
    # 숫자에 따라서 다른 값을 받고 싶은 경우 int:id로 path 정의 하기
    path("<int:id>",getDB),
    path("test/",getTest), #for test
    path('postTest/', postTest, name="postMember"), #for test
    # 재준 : rest API 형식에 맞춰서 url 생성
    # 재준 : CruxClimbingspot
    path('GET/spot/<int:id>',getSpot),
    path('POST/spot/',postSpot,name='postSpot'),
    # 재준 : CruxQuestion
    path('GET/question/<int:id>',getQuestion),
    path('POST/question/',postQuestion,name='postQuestion'),
    # 재준 : CruxSector
    path('GET/sector/<int:id>',getSector),
    path('POST/sector/',postSector,name='postSector'),
    # 재준 : CruxVideo
    path('GET/video/<int:id>',getVideo),
    path('POST/video/',postVideo,name='postVideo'),

    #민재: ForumPost,ForumRelpy,CruxUser
    path("GET/forumPost/<int:id>",getForumPost),
    path("POST/forumPost",postForumPost,name='postForumPost'),

    path("GET/forumReply/<int:id>",getForumRelpy),
    path("POST/forumReply",postForumRelpy,name='postForumReply'),

    path("GET/User/<char:id>",getUser),
    path("POST/User",postUser,name='postUser'), #필요성?
]

