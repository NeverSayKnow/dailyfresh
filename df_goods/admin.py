from django.contrib import admin
from .models import *


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ['goods_name', 'goods_id', 'goods_pic', 'goods_price']
    # 过滤的字段，过滤框会出现在右边
    list_filter = ['goods_name']
    # 搜索字段，出现在上面
    search_fields = ['goods_name']
    # 分页
    list_per_page = 10


@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['typename', 'type_id']
