$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function getName() {
        $.ajax({
            'url': '/new_name/',
            'method': 'GET',
            'dataType': 'json',
            'success': function (res) {
                $('#name0').html(res.name);
                $('#name1').html(res.name);
                $('#first').html(res.first);
                $('#second').html(res.second);
            },
            'error': function (res, code, jqxhr) {
                console.log(res);
                console.log(code);
                console.log(jqxhr);
            }
        })
    }

    $('#gbutton').click(function () {
        return getName();
    });
});