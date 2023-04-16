from django.db import models

# Create your models here.

# 재준 : mysql에 만든 테이블 불러오기
# 3개 진행 -> DB내용 불러오기 및 migration
# python manage.py inspectdb
# python manage.py makemigrations
# python manage.py migrate

class CruxClimbingspot(models.Model):
    spotid = models.PositiveIntegerField(db_column='SpotID', primary_key=True)  # Field name made lowercase.
    spotname = models.CharField(db_column='SpotName', max_length=30)  # Field name made lowercase.
    spotaddress = models.CharField(db_column='SpotAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRUX_Climbingspot'


class CruxQuestion(models.Model):
    questionid = models.PositiveIntegerField(db_column='QuestionID', primary_key=True)  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.
    questionimage = models.CharField(db_column='QuestionImage', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRUX_Question'


class CruxSector(models.Model):
    sectornum = models.PositiveIntegerField(db_column='SectorNum', primary_key=True)  # Field name made lowercase. The composite primary key (SectorNum, LocateSpotID) found, that is not supported. The first column is selected.
    locatespotid = models.ForeignKey(CruxClimbingspot, models.DO_NOTHING, db_column='LocateSpotID')  # Field name made lowercase.
    sectorimage = models.CharField(db_column='SectorImage', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRUX_Sector'
        unique_together = (('sectornum', 'locatespotid'),)


class CruxUser(models.Model):
    memberid = models.CharField(db_column='MemberID', primary_key=True, max_length=12)  # Field name made lowercase.
    memberpw = models.CharField(db_column='MemberPW', max_length=20)  # Field name made lowercase.
    membernickname = models.CharField(db_column='MemberNickname', max_length=20)  # Field name made lowercase.
    memberprofilepic = models.CharField(db_column='MemberProfilePic', max_length=50, blank=True, null=True)  # Field name made lowercase.
    memberprofileintro = models.TextField(db_column='MemberProfileIntro', blank=True, null=True)  # Field name made lowercase.
    memberprofilerecentque = models.TextField(db_column='MemberProfileRecentQue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRUX_User'


class CruxVideo(models.Model):
    videoid = models.PositiveIntegerField(db_column='VideoID', primary_key=True)  # Field name made lowercase.
    uploadmemid = models.ForeignKey(CruxUser, models.DO_NOTHING, db_column='UploadMemID')  # Field name made lowercase.
    uploaddate = models.DateField(db_column='UploadDate')  # Field name made lowercase.
    videourl = models.CharField(db_column='VideoURL', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRUX_Video'


class ForumPosts(models.Model):
    postsid = models.IntegerField(db_column='PostsID', primary_key=True)  # Field name made lowercase.
    postwritememid = models.CharField(db_column='PostWriteMemID', max_length=12)  # Field name made lowercase.
    writedate = models.DateField(db_column='WriteDate')  # Field name made lowercase.
    posttitle = models.TextField(db_column='PostTitle')  # Field name made lowercase.
    postcontent = models.TextField(db_column='PostContent')  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Forum_Posts'


class ForumRelpy(models.Model):
    replyid = models.PositiveIntegerField(db_column='ReplyID', primary_key=True)  # Field name made lowercase. The composite primary key (ReplyID, OriginPostID) found, that is not supported. The first column is selected.
    originpostid = models.ForeignKey(ForumPosts, models.DO_NOTHING, db_column='OriginPostID')  # Field name made lowercase.
    writterid = models.CharField(db_column='WritterID', max_length=12)  # Field name made lowercase.
    replycontent = models.TextField(db_column='ReplyContent')  # Field name made lowercase.
    replydate = models.DateField(db_column='ReplyDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Forum_Relpy'
        unique_together = (('replyid', 'originpostid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'