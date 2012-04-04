# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class NiftDbAttendance(models.Model):
    date = models.DateField()
    present = models.BooleanField()
    user_id = models.ForeignKey(NiftDbUser, primary_key=True)
    class Meta:
        db_table = u'nift_db_attendance'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class NiftDbAddress(models.Model):
    user_id = models.ForeignKey(NiftDbUser, primary_key=True)
    perm_street = models.CharField(max_length=200)
    perm_zip = models.SmallIntegerField()
    perm_state = models.CharField(max_length=50)
    temp_street = models.CharField(max_length=200)
    temp_zip = models.SmallIntegerField()
    temp_state = models.CharField(max_length=50)
    class Meta:
        db_table = u'nift_db_address'

class NiftDbCenDepInfo(models.Model):
    centre_name = models.CharField(max_length=50)
    department_name = models.CharField(max_length=50)
    cen_dep_info = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'nift_db_cen_dep_info'

class NiftDbOffered(models.Model):
    id = models.IntegerField(primary_key=True)
    sem_id = models.ForeignKey(NiftDbSemInfo)
    course_id = models.ForeignKey(NiftDbCourse)
    cen_dep_info = models.ForeignKey(NiftDbCenDepInfo)
    user_id = models.ForeignKey(NiftDbUser)
    class Meta:
        db_table = u'nift_db_offered'

class NiftDbSemInfo(models.Model):
    term = models.CharField(max_length=1)
    year = models.CharField(max_length=4)
    sem_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'nift_db_sem_info'

class NiftDbCourse(models.Model):
    course_name = models.CharField(max_length=50)
    course_id = models.CharField(max_length=20, primary_key=True)
    class Meta:
        db_table = u'nift_db_course'

class NiftDbTeaching(models.Model):
    sem_id = models.ForeignKey(NiftDbSemInfo)
    course_id = models.ForeignKey(NiftDbCourse)
    user_id = models.ForeignKey(NiftDbUser)
    study_type = models.CharField(max_length=1)
    detail_type = models.CharField(max_length=1)
    teaching_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'nift_db_teaching'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class NiftDbProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    join_date = models.DateField()
    designation = models.CharField(max_length=1)
    basic_pay = models.IntegerField()
    room_no = models.CharField(max_length=10)
    past_positions = models.CharField(max_length=150)
    experience = models.SmallIntegerField()
    expertise = models.CharField(max_length=150)
    class Meta:
        db_table = u'nift_db_profile'

class NiftDbUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    login_name = models.CharField(max_length=100, unique=True)
    sex = models.CharField(max_length=1)
    password = models.CharField(max_length=100)
    email_add = models.CharField(max_length=100)
    dob = models.DateField()
    phone_no = models.SmallIntegerField()
    user_id = models.CharField(max_length=100, primary_key=True)
    marital_status = models.CharField(max_length=100)
    class Meta:
        db_table = u'nift_db_user'

class NiftDbLeaveInfo(models.Model):
    leave_type = models.CharField(max_length=1)
    start_date = models.DateField()
    reason = models.CharField(max_length=1000)
    no_of_days = models.SmallIntegerField()
    approved = models.BooleanField()
    days_left = models.SmallIntegerField()
    user_id = models.ForeignKey(NiftDbUser)
    leave_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'nift_db_leave_info'

class NiftDbLeaveExtensionInfo(models.Model):
    last_leave_id = models.ForeignKey(NiftDbLeaveInfo)
    reason = models.CharField(max_length=1000)
    approved = models.BooleanField()
    eleave_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'nift_db_leave_extension_info'

