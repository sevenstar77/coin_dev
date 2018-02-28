from django.db import models
from .managers import MyaccountinfoManager
# Create your models here.

class Myaccountinfo(models.Model):
    no = models.IntegerField(db_column='no', blank=True, null=True)
    user_no = models.IntegerField(db_column='userno',)
    name = models.CharField(db_column='name', max_length=100)
    email = models.CharField(db_column='email', max_length=100)
    is_email_receive = models.CharField(db_column='isemailreceive', max_length=5)
    currency = models.CharField(db_column='currency', max_length=3)
    price = models.TextField(db_column='price', blank=True, null=True)  # This field type is a guess.
    amount = models.IntegerField(db_column='amount')
    first_insert_uno = models.IntegerField(db_column='firstinsertuno')
    first_insert_time = models.DateTimeField(db_column='firstinserttime')
    last_update_uno = models.IntegerField(db_column='lastupdateuno')
    last_update_time = models.DateTimeField(db_column='lastupdatetime')

    objects = MyaccountinfoManager()
    class Meta:
        managed = False
        db_table = 'myaccountinfo'
