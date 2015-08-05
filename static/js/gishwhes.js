$(document).ready(function () {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
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

    var lc = LC.init(document.getElementsByClassName('literally')[0],
        {imageURLPrefix: '/static/img'});
    var name = $('#name0').html();
    var first = $('#first').html();
    var second = $('#second').html();
    $('[data-action=upload-to-server]').click(function (e) {
        e.preventDefault();

        $('.submit').html('Uploading...');
        // data argument;
        $.ajax({
            url: '/img_up/',
            type: 'POST',
            data: {
                // convert the image data to base64
                image: lc.canvasForExport().toDataURL().split(',')[1],
                type: 'base64',
                title: name,
                first: first,
                second: second
            },
            success: function (result) {
                $('.submit').html('Uploaded!');
                $.ajax({
                    url: '/images/',
                    success: function (data) {
                        $('#images-refresh').html(data);
                    }
                });
            }
        });
    });

});