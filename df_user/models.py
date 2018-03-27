from django.db import models


# 用户
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_pwd = models.CharField(max_length=40)
    user_email = models.CharField(max_length=50,default='')
    user_phone = models.CharField(max_length=11, default='')

    class Meta:
        db_table = 'user'


# 收货地址
class DeliAddress(models.Model):
    deli_name = models.CharField(max_length=10)
    deli_address = models.CharField(max_length=80,default='')
    deli_postcode = models.CharField(max_length=6,default='')
    deli_phone = models.CharField(max_length=11,default='')
    user_id = models.IntegerField()

    class Meta:
        db_table = 'delivery_address'
