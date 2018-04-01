$(function () {

    var name_is_ok = false;
    var address_is_ok = false;
    var postcode_is_ok = false;
    var phone_is_ok = false;
    var is_modify = false;
    var modify_id = 0;

    function check_name() {
        // 检测姓名
        var re = /^[\u4e00-\u9fa5]+(·[\u4e00-\u9fa5]+)*$/;
        if (re.test($('#deli_name').val())) {
            name_is_ok = true;
        } else {
            alert('名字输入不合规');
            name_is_ok = false;
        }
    }

    function check_address() {
        // 检测姓名

        if (($('#deli_address').val()).length >= 5) {
            address_is_ok = true;
        } else {
            alert('地址输入不合规');
            address_is_ok = false;
        }
    }

    function check_postcode() {
        // 检测姓名
        var re = /^\d{6}$/;
        if (re.test($('#deli_postcode').val())) {
            postcode_is_ok = true;
        } else {
            alert('邮政编码输入有误');
            postcode_is_ok = false;
        }
    }

    function check_phone() {
        // 检测姓名
        var re = /^[1][34578][0-9]{9}$/;
        if (re.test($('#deli_phone').val())) {
            phone_is_ok = true;
        } else {
            alert('手机号输入不正确');
            phone_is_ok = false;
        }
    }

    // $('#is_default').click(function () {
    //     alert($(this).prop('checked'))
    // });

    // 提交表单--添加地址
    $('#form_info').submit(function (event) {
        event.preventDefault();
        check_name();
        check_address();
        check_postcode();
        check_phone();

        if (name_is_ok && address_is_ok && postcode_is_ok && phone_is_ok) {
            // 判断是添加还是修改地址
            if (is_modify) {
                if (modify_id === 0) {
                    return false
                }
                var is_default;
                // 设置是否选择默认地址的值，因为django中的布尔值为False/True,js中为false/true,需要转换一下
                if($('#is_default').prop('checked')){
                    is_default = 'True'
                }else {
                    is_default = 'False'
                }
                var data = {
                    "id": modify_id,
                    "deli_name": $('#deli_name').val(),
                    "deli_address": $('#deli_address').val(),
                    "deli_postcode": $('#deli_postcode').val(),
                    "deli_phone": $('#deli_phone').val(),
                    "is_default": is_default,
                    "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val() // 设置csrf,不然请求不成功
                };
                $.ajax({
                    url: '/user/user_center_address/modify/',
                    type: 'POST',
                    dataType: 'json',
                    async: true,//异步加载数据
                    data: data
                })
                    .done(function (data) {
                        if (data.code === 200) {
                            alert(data.message);
                            location.reload() //刷新当前页面
                        }
                    })
                    .fail(function () {
                        alert('服务器超时，请重试！');
                    });
            } else { //添加地址
                $.ajax({
                    url: '/user/user_center_address/add/',
                    type: 'POST',
                    dataType: 'json',
                    async: true,//异步加载数据
                    data: $(this).serialize()
                })
                    .done(function (data) {
                        if (data.code === 200) {
                            location.reload() //刷新当前页面
                        }
                    })
                    .fail(function () {
                        alert('服务器超时，请重试！');
                    })
            }
        } else {
            return false
        }
    });

    //点击修改地址(应用时间委托)
    $('#add_list').on('click', 'button', function () {
        // alert($(this).attr("id"));
        var id = $(this).attr("id");
        //判断是修改(m)还是删除(d)--例如id为m123或者d22,后面的数字为地址id
        //其实可以不用再次请求获取，这里是想练一下ajax
        if (id[0] === "m") {
            is_modify = true;
            $.ajax({
                url: '/user/user_center_address/one/',
                type: 'GET',
                dataType: 'json',
                async: true,//异步加载数据
                data: {"id": id.substring(1)}
            })
                .done(function (data) {
                    // alert(data['code']);
                    if (data.code === 200) {
                        is_modify = true;
                        var address = data.data[0];
                        modify_id = address['pk'];
                        // alert(modify_id);
                        $('#deli_name').val(address.deli_name);
                        $('#deli_address').val(address.deli_address);
                        $('#deli_postcode').val(address.deli_postcode);
                        $('#deli_phone').val(address.deli_phone);
                    }
                })
                .fail(function () {
                    alert('服务器超时，请重试！');
                })
        } else {
            $.ajax({
                url: '/user/user_center_address/delete/',
                type: 'GET',
                dataType: 'json',
                async: true,//异步加载数据
                data: {"id": id.substring(1)}
            })
                .done(function (data) {
                    // alert(data['code']);
                    if (data.code === 200) {
                        alert(data.message);
                        location.reload();
                    }
                })
                .fail(function () {
                    alert('服务器超时，请重试！');
                })
        }
    })
});