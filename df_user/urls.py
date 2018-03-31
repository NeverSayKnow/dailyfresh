from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/register/', views.register, name='redirect'),
    path('user/register_handle/', views.register_handle, name='register_handle'),
    path('user/login/', views.login, name='login'),
    path('user/login_handle/', views.login_handle, name='login_handle'),
    path('user/user_center_info/', views.user_center_info, name='user_center_info'),
    path('user/user_center_order/', views.user_center_order, name='user_center_order'),
    path('user/user_center_address/', views.user_center_address, name='user_center_address'),
    path('user/user_center_address/add/', views.user_add_address, name='user_add_address'),
]

app_name = 'df_user'
