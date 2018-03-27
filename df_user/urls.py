from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/register/', views.register, name='redirect'),
    path('user/register_handle/', views.register_handle, name='register_handle'),
    path('user/login/', views.login, name='login'),
    path('user/login_handle/', views.login_handle, name='login_handle'),
    path('user/user_info/', views.user_info, name='user_info'),
]

app_name = 'df_user'
