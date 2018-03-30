from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from hashlib import sha1


# 首页
def index(request):
    return render(request, 'df_user/index.html', {'Title': '天天生鲜-首页'})


# 用户注册
def register(request):
    return render(request, 'df_user/register.html', {'Title': '天天生鲜-注册'})


# 判断是否为post请求
def is_post(func):
    def is_post_inner(request):
        if request.method != 'POST':
            return JsonResponse({"code": 201, "message": '该请求不是post请求', "data": {}})
        return func(request)
    return is_post_inner


# 处理用户注册
@is_post
def register_handle(request):
    post = request.POST
    # 对比两次密码是否输入一样
    pwd = post['pwd']
    cpwd = post['cpwd']
    if pwd != cpwd:
        return JsonResponse({"code": 202, "message": '两次密码输入不一致', "data": {}})
    # 创建用户对象
    user = User()
    user.user_name = post["user_name"]
    user.user_email = post["email"]
    # 密码进行sha1加密
    s1 = sha1()
    s1.update(pwd.encode())
    user.user_pwd = s1.hexdigest()
    user.save()
    return redirect('/user/login/')


# 用户名是否重复
def register_exist(request):
    name = request.GET['name']
    count = User.objects.filter(user_name=name).count()  # 返回1则说明已经存在，0则不存在
    return JsonResponse({"code": 200, "message": 'OK', "data": {"count": count}})


# 用户登录
def login(request):
    # 查看cookie中是否存有用户名
    user_name = request.COOKIES.get('user_name', '')
    # print(user_name)  # 测试能否获取cookie中的名字
    return render(request, 'df_user/login.html', {"Title": "天天生鲜-登录", "user_name": user_name})


# 用户登录处理(登录成功进入用户中心)
@is_post
def login_handle(request):
    # if request.method != 'POST':
    #     return render(request, 'df_user/login.html', {"code": 201, "message": '该请求不是post请求', "data": {}})
    post = request.POST
    user_name = post.get('username')
    print(user_name)
    # 判断数据库中是否有该用户
    user = User.objects.filter(user_name=user_name)
    # print(len(user))
    if len(user) == 0:
        return JsonResponse({"code": 203, "message": '用户不存在', "data": {}})
    # 如果用户存在，创建跳转对象，若密码正确，接下来跳转到用户详情界面
    # response = HttpResponseRedirect('/user/user_center_info/')
    data = {}
    is_remember = post.get('is_remember', '0')
    pwd = post.get('pwd')

    # 判断用户输入密码是否正确
    s = sha1()
    s.update(pwd.encode())
    pwd_sha1 = s.hexdigest()
    if pwd_sha1 != user[0].user_pwd:
        return JsonResponse({"code": 204, "message": '密码输入错误，请重试', "data": {}})

    # data['code'] = 200
    # data["message"] = '登录成功'
    # data["data"] = {"uid":user[0].pk}
    response = JsonResponse({"code": 200, "message": '登录成功', "data": {"uid":user[0].pk}})

    request.session['uname'] = post.get('username')  # 将用户名存进session中
    request.session.set_expiry(0)  # 关闭浏览器失效
    # 判断是否记住用户名
    if is_remember == '1':
        # 将用户名存入cookie
        response.set_cookie('user_name', user_name, max_age=604800)  # 过期时间为一个星期
    else:
        response.set_cookie('user_name', user_name, max_age=-1)

    # print('================')

    return response


# 用户中心--个人信息
def user_center_info(request):
    uname = request.session.get('uname', '')
    if uname == '':
        # print('返回登录')
        user_name = request.COOKIES.get('user_name', '')
        return redirect('/user/login/')  # 返回登录
    return render(request, 'df_user/user_center_info.html', {"Title": "天天生鲜-用户中心"})


# 用户中心--全部订单
def user_center_order(request):
    return render(request, 'df_user/user_center_order.html', {"Title": "天天生鲜-用户中心"})


# 用户中心--收货地址
def user_center_address(request):
    return render(request, 'df_user/user_center_site.html', {"Title": "天天生鲜-用户中心"})



