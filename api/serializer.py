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

# 재준 : 클라이밍장 리스트를 받아오기 위한 serializer        
class SpotNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxClimbingspot
        fields = ['spotname']
      
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

# 재준 : 최근 검색 암장을 받아오기위한 sericalizer
class RecentSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxUser
        fields = ['memberprofilerecentque']


#민재: 게시판(크루/자유), 마이페이지 기능구현용 serializer 생성    
#ForumPost, ForumReply, CruxUser       
class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPosts
        fields = '__all__'

class ForumRelpySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumRelpy
        fields = '__all__'

class CruxUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CruxUser
        fields = '__all__'
