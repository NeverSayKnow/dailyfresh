from django.db import models
from tinymce.models import HTMLField


# 商品类型
class GoodsType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    # 在admin中显示标题列名称
    def typename(self):
        return self.type_name

    typename.short_description = '商品类型'

    class Meta:
        db_table = 'goods_type'


# 商品
class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=30)
    goods_pic = models.ImageField(upload_to='df_goods/')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)
    goods_unit = models.CharField(max_length=10)
    goods_intro = models.CharField(max_length=70)
    goods_detail = HTMLField()
    goods_click = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        db_table = 'goods'
