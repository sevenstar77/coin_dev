from django.db import models
from .managers import EmailscheduleManager, SchedulemasterManager
# Create your models here.


class Emailschedule(models.Model):
    no = models.IntegerField(db_column='no',  primary_key=True)
    user_no = models.IntegerField(db_column='userno', blank=True, null=True)
    name = models.CharField(db_column='name', max_length=100)
    email = models.CharField(db_column='email', max_length=100)
    is_email_receive = models.CharField(db_column='IsEmailReceive', max_length=5)  # Field name made lowercase.
    schedule_type = models.CharField(db_column='scheduletype', max_length=20)
    currency = models.CharField(db_column='currency', max_length=3)
    from_date = models.DateTimeField(db_column='fromdate')
    to_date = models.DateTimeField(db_column='todate')
    first_insert_uno = models.IntegerField(db_column='FirstInsertUno')  # Field name made lowercase.
    first_insert_time = models.DateTimeField(db_column='FirstInsertTime')  # Field name made lowercase.
    last_update_uno = models.IntegerField(db_column='LastUpdateUno')  # Field name made lowercase.
    last_update_time = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.

    objects = EmailscheduleManager()

    class Meta:
        managed = False
        db_table = 'emailschedule'

class Schedulemaster(models.Model):
    no = models.IntegerField(db_column='no',  primary_key=True)
    user_no = models.IntegerField(db_column='userno')
    name = models.CharField(db_column='name', max_length=100)
    email = models.CharField(db_column='email', max_length=100)
    is_email_receive = models.CharField(db_column='isemailreceive', max_length=5)
    schedule_type = models.CharField(db_column='scheduletype', max_length=10)
    currency = models.CharField(db_column='currency', max_length=3)
    price = models.DecimalField(db_column='price', max_digits=15, decimal_places=2, blank=True, null=True)  # This field type is a guess.
    target_up_price = models.DecimalField(db_column='targetupprice', max_digits=15, decimal_places=2,  blank=True, null=True)  # This field type is a guess.
    target_down_price = models.DecimalField(db_column='targetdownprice', max_digits=15, decimal_places=2,  blank=True, null=True)  # This field type is a guess.
    target_up_percent = models.IntegerField(db_column='targetuppercent', blank=True, null=True)
    target_down_percent = models.IntegerField(db_column='targetdownpercent', blank=True, null=True)
    from_date = models.DateTimeField(db_column='fromdate')
    to_date = models.DateTimeField(db_column='todate')
    first_insert_uno = models.IntegerField(db_column='firstinsertuno')
    first_insert_time = models.DateTimeField(db_column='firstinserttime')
    last_update_uno = models.IntegerField(db_column='lastupdateuno')
    last_update_time = models.DateTimeField(db_column='lastupdatetime')

    objects = SchedulemasterManager()

    class Meta:
        managed = False
        db_table = 'scheduleMaster'
