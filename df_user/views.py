from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from hashlib import sha1


# 首页
def index(request):
    return render(request, 'df_user/index.html', {'Title': '天天生鲜-首页'})


# 用户注册
def register(request):
    return render(request, 'df_user/register.html', {'Title': '天天生鲜-注册'})


# 处理用户注册
def register_handle(request):
    if request.method != 'POST':
        return HttpResponse({'code': 201, 'message': '该请求不是post请求', 'data': {}})
    post = request.POST
    # 对比两次密码是否输入一样
    pwd = post['pwd']
    cpwd = post['cpwd']
    if pwd != cpwd:
        return HttpResponse({'code': 202, 'message': '两次密码输入不一致', 'data': {}})
    # 创建用户对象
    user = User()
    user.user_name = post["user_name"]
    user.user_email = post["email"]
    # 密码进行sha1加密
    s1 = sha1()
    s1.update(pwd.encode())
    user.user_pwd = s1.hexdigest()
    user.save()
    return redirect('/login/')


# 用户名是否重复
def register_exist(request):
    name = request.GET['name']
    count = User.objects.filter(user_name=name).count()  # 返回1则说明已经存在，0则不存在
    return HttpResponse({'code': 200, 'message': 'OK', 'data': {'count': count}})


# 用户登录
def login(request):
    return render(request, 'df_user/login.html', {"Title": "天天生鲜-登录"})


# 用户登录处理(登录成功进入用户中心)
def login_handle(request):
    if request.method != 'POST':
        return HttpResponse({'code': 201, 'message': '该请求不是post请求', 'data': {}})
    post = request.POST

    return redirect('/user_info/')


# 用户中心
def user_info(request):
    return render(request, 'df_user/user_center_info.html', {"Title": "天天生鲜-用户中心"})
