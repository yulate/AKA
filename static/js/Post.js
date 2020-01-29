function post(url, params) {
    var temp = document.createElement("form");
    temp.action = url;
    temp.method = "post";
    temp.style.display = "none";
    for ( var x in params) {
        var opt = document.createElement("input");
        opt.name = x;
        opt.value = params[x];
        temp.appendChild(opt);
    }
    document.body.appendChild(temp);
    temp.submit();
    return temp;
}

function video_list_send(value) {
    post(
        "http://39.105.204.201/fiction/fiction_data/",
        {
            xsurl1 : value
        });
}
function video_data_send(value) {
    post(
        "http://39.105.204.201/fiction/fiction_show/",
        {
            xsurl2 : value
        });
}

function cartoon_list_send(value) {
    post(
        "http://39.105.204.201/cartoon/cartoon_data/",
        {
            mhurl1 : value
        });
}
function cartoon_data_send(value) {
    post(
        "http://39.105.204.201/cartoon/cartoon_show/",
        {
            mhurl2 : value
        });
}

function fiction_list_send(value) {
    post(
        "http://39.105.204.201/fiction/fiction_data/",
        {
            xsurl1 : value
        });
}
function fiction_data_send(value) {
    post(
        "http://39.105.204.201/fiction/fiction_show/",
        {
            xsurl2 : value
        });
}