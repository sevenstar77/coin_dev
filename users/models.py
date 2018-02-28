from django.db import models
from .auth.custom_user_model import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Usermaster(AbstractBaseUser):
    user_no = models.IntegerField(db_column='userno', primary_key=True)  # Field name made lowercase.
    user_status_code = models.CharField(db_column='userstatuscode', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=100)  # Field name made lowercase.
    id = models.CharField(db_column='id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_password = models.CharField(db_column='userpassword', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mobile_phone_no = models.CharField(db_column='mobilephoneno', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='emailaddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    is_email_receive = models.CharField(db_column='isemailreceive', max_length=5)  # Field name made lowercase.
    enter_join_time = models.DateTimeField(db_column='enterjointime')  # Field name made lowercase.
    last_update_uno = models.IntegerField(db_column='lastupdateuno')  # Field name made lowercase.
    last_update_time = models.DateTimeField(db_column='lastupdatetime')  # Field name made lowercase.

    USERNAME_FIELD = 'user_no'
    REQUIRED_FIELDS = []
    temp_password = None


    class Meta:
        managed = False
        db_table = 'usermaster'
        #verbose_name = _('user')
        #verbose_name_plural = _('users')

    # class Usermaster(models.Model):
    #     userno = models.IntegerField(blank=True, null=True)
    #     userstatuscode = models.CharField(max_length=10, blank=True, null=True)
    #     name = models.CharField(max_length=100)
    #     id = models.CharField(max_length=100)
    #     userpassword = models.CharField(max_length=1000, blank=True, null=True)
    #     gender = models.CharField(max_length=1, blank=True, null=True)
    #     mobilephoneno = models.CharField(max_length=30, blank=True, null=True)
    #     emailaddress = models.CharField(max_length=100, blank=True, null=True)
    #     isemailreceive = models.CharField(max_length=5)
    #     enterjointime = models.DateTimeField()
    #     lastupdateuno = models.IntegerField(blank=True, null=True)
    #     lastupdatetime = models.DateTimeField()
    #
    #     class Meta:
    #         managed = False
    #         db_table = 'usermaster'
