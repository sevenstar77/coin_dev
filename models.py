# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class Emailschedule(models.Model):
    no = models.IntegerField(blank=True, null=True)
    userno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    isemailreceive = models.CharField(db_column='IsEmailReceive', max_length=5)  # Field name made lowercase.
    scheduletype = models.CharField(max_length=20)
    currency = models.CharField(max_length=3)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    firstinsertuno = models.IntegerField(db_column='FirstInsertUno')  # Field name made lowercase.
    firstinserttime = models.DateTimeField(db_column='FirstInsertTime')  # Field name made lowercase.
    lastupdateuno = models.IntegerField(db_column='LastUpdateUno')  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emailschedule'


class Myaccountinfo(models.Model):
    no = models.IntegerField(blank=True, null=True)
    userno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    isemailreceive = models.CharField(max_length=5)
    currency = models.CharField(max_length=3)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    amount = models.IntegerField()
    firstinsertuno = models.IntegerField()
    firstinserttime = models.DateTimeField()
    lastupdateuno = models.IntegerField()
    lastupdatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'myaccountinfo'


class Ordermaster(models.Model):
    no = models.IntegerField(blank=True, null=True)
    userno = models.IntegerField()
    order_id = models.CharField(max_length=200)
    price = models.TextField()  # This field type is a guess.
    qty = models.TextField()  # This field type is a guess.
    currency = models.CharField(max_length=3)
    orderstatus = models.CharField(max_length=10)
    firstinsertuno = models.IntegerField()
    firstinserttime = models.DateTimeField()
    lastupdateuno = models.IntegerField()
    lastupdatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ordermaster'


class Schedulemaster(models.Model):
    no = models.IntegerField(blank=True, null=True)
    userno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    isemailreceive = models.CharField(max_length=5)
    scheduletype = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    targetupprice = models.TextField(blank=True, null=True)  # This field type is a guess.
    targetdownprice = models.TextField(blank=True, null=True)  # This field type is a guess.
    targetuppercent = models.IntegerField(blank=True, null=True)
    targetdownpercent = models.IntegerField(blank=True, null=True)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    firstinsertuno = models.IntegerField()
    firstinserttime = models.DateTimeField()
    lastupdateuno = models.IntegerField()
    lastupdatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scheduleMaster'


class Usermaster(models.Model):
    userno = models.IntegerField(blank=True, null=True)
    userstatuscode = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=1000, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    mobilephoneno = models.CharField(max_length=30, blank=True, null=True)
    emailaddress = models.CharField(max_length=100, blank=True, null=True)
    isemailreceive = models.CharField(max_length=5)
    enterjointime = models.DateTimeField()
    lastupdateuno = models.IntegerField(blank=True, null=True)
    lastupdatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usermaster'
