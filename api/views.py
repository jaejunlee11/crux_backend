from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializer import *


# Create your views here.
@api_view(['GET'])
def API(request):
    return Response("test")


# 재준 : db데이터를 가져오는 것 확인 (그냥 가져오는 경우 jason type이 아니라 오류 발생)
# 재준 : serializer를 통해서 jason으로 변경 후 가져옴
@api_view(['GET'])
def getTest(request):
    test=Test.objects.all()
    serializer = TestSerializer(test, many=True)
    return Response(serializer.data)

# 재준 : db데이터를 가져오는 GET 생성 원하는 id와 일치하는 것만 가져옴(테스트 완료)
# id값을 활용하여 id가 일치하는 정보만 GET해옴(성공)
@api_view(['GET'])
def getDB(request,id):
    test=Test.objects.filter(id=id)
    serializer = TestSerializer(test, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getForumPost(request):
    forumPost=ForumPosts.objects.all()
    serializer = ForumPostSerializer(forumPost, many=True)
    return Response(serializer.data)

# 재준 : db에 데이터를 넣는 것 테스트 확인 완료
# 해당 틀에 맞춰서 작성 해줘야함
"""
{
"id" : 2,
"name" : "jaejun"
}
"""
@api_view(['POST'])
def postTest(request):
    reqData = request.data
    serializer = TestSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 재준 : CruxClimbingspot 데이터 GET, POST
@api_view(['GET'])
def getSpot(request,id):
    test=CruxClimbingspot.objects.filter(spotid=id)
    serializer = CruxClimbingspotSerializer(test, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postSpot(request):
    reqData = request.data
    serializer = CruxClimbingspotSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 재준 : CruxQuestion 데이터 GET, POST
@api_view(['GET'])
def getQuestion(request,id):
    test=CruxQuestion.objects.filter(questionid=id)
    serializer = CruxQuestionSerializer(test, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postQuestion(request):
    reqData = request.data
    serializer = CruxQuestionSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 재준 : CruxSector 데이터 GET, POST
@api_view(['GET'])
def getSector(request,id):
    test=CruxSector.objects.filter(sectornum=id)
    serializer = CruxSectorSerializer(test, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postSector(request):
    reqData = request.data
    serializer = CruxSectorSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 재준 : CruxVideo 데이터 GET, POST
@api_view(['GET'])
def getVideo(request,id):
    test=CruxVideo.objects.filter(videoid=id)
    serializer = CruxVideoSerializer(test, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postVideo(request):
    reqData = request.data
    serializer = CruxVideoSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)