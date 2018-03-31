$(function () {

    var name_is_ok = false;
    var address_is_ok = false;
    var postcode_is_ok = false;
    var phone_is_ok = false;

    function check_name() {
        // 检测姓名
        var re = /^[\u4e00-\u9fa5]+(·[\u4e00-\u9fa5]+)*$/;
        if(re.test($('#deli_name').val())){
            name_is_ok = true;
        }else {
            alert('名字输入不合规');
            name_is_ok = false;
        }
    }

    function check_address() {
        // 检测姓名

        if(($('#deli_address').val()).length>=5){
            address_is_ok = true;
        }else {
            alert('地址输入不合规');
            address_is_ok = false;
        }
    }

    function check_postcode() {
        // 检测姓名
        var re = /^\d{6}$/;
        if(re.test($('#deli_postcode').val())){
            postcode_is_ok = true;
        }else {
            alert('邮政编码输入有误');
            postcode_is_ok = false;
        }
    }

    function check_phone() {
        // 检测姓名
        var re = /^[1][34578][0-9]{9}$/;
        if(re.test($('#deli_phone').val())){
            phone_is_ok = true;
        }else {
            alert('手机号输入不正确');
            phone_is_ok = false;
        }
    }

    $('#form_info').submit(function (event) {
        event.preventDefault();
        check_name();
        check_address();
        check_postcode();
        check_phone();

        if(name_is_ok && address_is_ok && postcode_is_ok && phone_is_ok){
            $.ajax({
                url: '/user/user_center_address/add/',
                type: 'POST',
                dataType: 'json',
                async: true,//异步加载数据
                data: $(this).serialize()
            })
                .done(function (data) {
                    location.reload() //刷新当前页面
                })
                .fail(function () {
                    alert('服务器超时，请重试！');
                })
        }else {
            return false
        }
    })

});