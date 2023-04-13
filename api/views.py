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

# 재준 : db데이터를 가져오는 GET 생성
# id값을 활용하여 여기서 사용 가능(test용으로 여기서는 사용 X)
@api_view(['GET'])
def getDB(request,id):
    permissions=AuthGroupPermissions.objects.all()
    return Response(permissions)


# 재준 : db데이터를 가져오는 것 확인 (그냥 가져오는 경우 jason type이 아니라 오류 발생)
# 재준 : serializer를 통해서 jason으로 변경 후 가져옴
@api_view(['GET'])
def getTest(request):
    test=Test.objects.all()
    serializer = TestSerializer(test, many=True)
    return Response(serializer.data)

# 재준 : db에 데이터를 넣는 것 테스트

@api_view(['POST'])
def postTest(request):
    reqData = request.data
    serializer = TestSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
