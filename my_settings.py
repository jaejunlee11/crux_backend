# 재준 : django 프로젝트 생성 DB연결
# 민재 : DB테이블 작성(MYSQL) 예정
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crux', # db이름
        'USER': 'root', # 로그인-유저 명
        'PASSWORD': '00000000',# 로그인- 비밀번호
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}