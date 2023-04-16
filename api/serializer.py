from rest_framework import serializers
from .views import *

# 재준 : jason 파일로 바꿔주기 위해서 serializer 생성
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        
class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPosts
        fields = '__all__'
      