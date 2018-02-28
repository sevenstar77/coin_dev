from django.db import models
from .managers import OrdermasterManger
# Create your models here.
class Ordermaster(models.Model):
    no = models.IntegerField(db_column="no", primary_key=True)
    user_no = models.IntegerField(db_column="userno")
    order_id = models.CharField(db_column="order_id", max_length=200)
    price = models.TextField(db_column="price")  # This field type is a guess.
    qty = models.TextField(db_column="qty")  # This field type is a guess.
    currency = models.CharField(db_column="currency", max_length=3)
    order_status = models.CharField(db_column="orderstatus", max_length=10)
    first_insert_uno = models.IntegerField(db_column="firstinsertuno")
    first_insert_time = models.DateTimeField(db_column="firstinserttime")
    last_update_uno = models.IntegerField(db_column="lastupdateuno")
    last_update_time = models.DateTimeField(db_column="lastupdatetime")

    objects = OrdermasterManger()

    class Meta:
        managed = False
        db_table = 'ordermaster'
