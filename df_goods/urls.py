from django.urls import path
from . import views

urlpatterns = [
    path('goods/list<int:gtype>_<int:sort>_<int:page>/', views.show_goods, name='show_goods'),
    path('goods/detail<int:goods_id>', views.goods_detail, name='goods_detail'),
]

app_name = 'df_goods'
