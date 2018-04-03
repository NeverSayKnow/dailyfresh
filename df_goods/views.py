from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# 商品列表页
def show_goods(request, gtype, sort, page):
    """
    :param request:
    :param gtype: 商品类型
    :param sort: 按照什么排序0--默认(最新产品)，1--价格(从低到高)，2--人气(点击量)
    :param page: 页数
    """
    goods = Goods.objects.filter(type_id=gtype)
    count = goods.count()
    news = []
    if count > 2:
        news = goods.order_by('-goods_id')[0:2]
    goods_list = []
    if sort == 0:
        goods_list = goods.order_by('-goods_id')
    elif sort == 1:
        goods_list = goods.order_by('goods_price')
    elif sort == 2:
        goods_list = goods.order_by('-goods_click')
    p = Paginator(goods_list, 10)
    goods_list_page = p.page(page)
    plist = p.page_range

    data = {"Title": '天天生鲜-商品列表',
            "has_cart": 1,
            "news": news,
            "goods_list_page": goods_list_page,
            "gtype": gtype,
            "sort": sort,
            "page_now": page,
            "num_pages": p.num_pages,
            "plist": plist}
    return render(request, 'df_goods/list.html', data)


# 商品详情页
def goods_detail(request, goods_id):
    goods = Goods.objects.get(goods_id=goods_id)
    news = Goods.objects.filter(type_id=goods.type_id).order_by('-goods_id')[0:2]
    data = {
        "Title": "天天生鲜-商品详情",
        "has_cart": 1,
        "goods": goods,
        "news": news
    }
    return render(request, 'df_goods/detail.html', data)
