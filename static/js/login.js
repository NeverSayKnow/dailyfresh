$(function () {

    var name_is_null = true;
    var pwd_is_null = true;
    var $name_input = $('.name_input');

    var name = $.cookie('user_name'); //从cookie中获取user_name 若没这个cookie打log显示的undefined
    console.log(name);
    $name_input.attr({'value':name}); //设置到输入框中

    //判断名字是否为空
    function nameIsNull() {
        var $name = $('.name_input');
        console.log($name.val());
        if ($name.val() === '') {
            $name.next().show();
        } else {
            name_is_null = false;
        }
    }

    // 获得焦点时隐藏提示
    $name_input.focus(function () {
        $(this).next().hide();
    });

    //判断密码是否为空
    function pwdIsNull() {
        var $pwd = $('.pass_input');
        console.log($pwd.val());
        if ($pwd.val() === '') {
            $pwd.next().show();
        } else {
            pwd_is_null = false;
        }
    }

    // 获得焦点时隐藏提示
    $('.pass_input').focus(function () {
        $(this).next().hide();
    });

    $('#login_form').submit(function (event) {
        event.preventDefault();
        nameIsNull();
        pwdIsNull();
        console.log(name_is_null +''+ pwd_is_null);
        if (!name_is_null && !pwd_is_null) {
            $.ajax({
                url: '/user/login_handle/',
                type: 'POST',
                dataType: 'json',
                async: false,//同步加载数据,发送请求时锁住浏览器,需要锁定用户交互操作时使用同步方式
                data: $(this).serialize()
            })
                .done(function (data) {
                    // alert(data.code);
                    var code = data.code;
                    if(code === 200){
                        location.href='/user/user_center_info/';//跳转到用户详情页面
                    }else if(code === 203){
                        $('.name_input').next().text(data.message).show();
                    }else if(code === 204){
                        $('.pass_input').next().text(data.message).show();
                    }
                })
                .fail(function () {
                    alert('服务器超时，请重试！');
                });
        }else {
            return false;
        }
    });

});