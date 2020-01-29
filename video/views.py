import requests
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
# 表单
from api.models import UV


def search_form(request):
    list = UV.objects.all()
    for var in list:
        ts = var.uv

    UV.objects.filter(id = 5).update(uv = ts + 1)

    for v in list:
        t = v.uv

    connect = {
        'text':t,
    }

    return render(request,'video/PlayVideo.html',connect)


# 接收请求数据
# def search(request):
#     request.encoding = 'utf-8'
#     if 'q' in request.GET:
#         message = request.GET['q'].encode('utf-8')
#     else:
#         message = '你提交了空表单'
#
#     connect = {
#         'message': message,
#     }
#     print(connect)
#     return render(request, "api/video.html", connect)


def get_yss(request):
    target = "http://api.pingcc.cn/?"
    name = "ysname=" + request.POST['name']
    url1 = target + name
    print(url1)
    req = requests.get(url1)
    a = req.json()
    res = a.get('list')
    print(res)
    connect = {
        'context': res
    }
    return render(request, 'video/list.html', connect)


def video(request):
    target = "http://api.pingcc.cn/?"
    genre_list = ['韩国剧', '海外剧', '欧美剧', '国产剧', '连续剧', '动漫', '国产动漫', '日韩动漫', '欧美动漫', '日本剧', '动漫片']
    get_url = request.GET.get('ysurl')
    get_genre = request.GET.get('genre')
    url = target + "ysurl=" + get_url
    print(url)
    req = requests.get(url)
    print(req)
    jsons = req.json()
    list = jsons.get('list')
    connect = {
        'message': list,
    }
    print(connect)
    if get_genre in genre_list:
        return render(request, 'video/series_list.html', connect)
    else:
        return render(request, 'video/video.html', connect)


def series(request):
    m3u8url = request.GET.get('m3u8url')
    onlineurl = request.GET.get('onlineurl')
    download = request.GET.get('download')
    num = request.GET.get('num')
    connect = {
        'm3u8url': m3u8url,
        'onlineurl': onlineurl,
        'download': download,
        'num': num
    }
    return render(request, 'video/play_series.html', connect)
    # return HttpResponse(m3u8url)


def Development_log(request):
    return render_to_response('Development_log.html')


def test(request):
    return render_to_response('test.html')

def deletes(request):
    UV.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")

def adds(request):
    addss = UV(uv = 1)
    addss.save()
    return HttpResponse("<p>数据添加成功！</p>")