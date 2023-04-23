from rest_framework import serializers
from .views import *

# 재준 : jason 파일로 바꿔주기 위해서 serializer 생성
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

# 재준 : 클라이밍장 검색 화면, 섹터 선택 화면, 문제 선택 화면, 동영상 확인 화면 구현을 위한 serializer생성
# 재준 : CruxClimbingspot, CruxQuestion, CruxSector, CruxVideo
class CruxClimbingspotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxClimbingspot
        fields = '__all__'
      
class CruxQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxQuestion
        fields = '__all__'

class CruxSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxSector
        fields = '__all__'

class CruxVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxVideo 
        fields = '__all__'
    
        
class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPosts
        fields = '__all__'
      