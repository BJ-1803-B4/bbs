$(function () {
    let $html = document.getElementsByTagName('html')[0];

    let offset = 20,
        start = 20,
        getjson_switch = 1,
        api_url = 'http://127.0.0.1:8000/index/get_posts',
        post_detail_url = 'http://127.0.0.1:8000/index/post_detail/';


    // 滚动条回顶部
    $(document).on('click', '#to_top', function () {
        $html.scrollTop = 0;
    });

    function scroll_fun() {
        let h1 = $html.scrollHeight,
            h2 = $html.scrollTop,
            h3 = $html.clientHeight;

        if (h1 < h2 + h3 + 200 && getjson_switch === 1) {
            getjson_switch = 0;
            $.getJSON(api_url, {'offset': offset, 'start': start}, function (json_data) {
                let post_list = JSON.parse(json_data['data']);

                if (post_list.length !== 0) {
                    for (let i = 0; i < post_list.length; i++) {
                        let post_url = post_detail_url + String(post_list[i]['pk']),
                            title = post_list[i]['fields']['title'],
                            author = post_list[i]['fields']['author'],
                            cont_str = post_list[i]['fields']['cont_str'],
                            timestamp = post_list[i]['fields']['timestamp'],
                            $post = "<li>" +
                                    "<p>" +
                                    "<span>标题：" + "<a href='"+ post_url +"'>" + title + "</a></span>" +
                                    "<span>日期：" + timestamp + "</span>" +
                                    "<span>作者：" + author + "</span>" +
                                    "</p>" +
                                    "<p>正文：" + cont_str + "</p>" +
                                    "</li>";
                        $('#post_ul').append($post);
                    }
                    start += offset;
                    setTimeout(function () {
                        getjson_switch = 1;
                    }, 1000);
                } else {
                    console.log('没有帖子了');
                    $('#post_ul').append('<li id="bottom_div">只有这么多了...</li>');
                }
            })
        }
    }

    $(document).scroll(scroll_fun);

});