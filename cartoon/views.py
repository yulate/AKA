import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request,'Cartoon/cartoon_index.html')

def get_cartoon(request):
    target = "http://api.pingcc.cn/?"
    mhname = "mhname=" + request.POST['mhname']
    urls = target + mhname
    req = requests.get(urls)
    a = req.json()
    res = a.get('list')
    print(res)
    connect = {
        'context': res
    }
    return render(request, 'Cartoon/cartoon_list.html', connect)

@method_decorator(csrf_exempt)
def cartoon_data(request):
    target = "http://api.pingcc.cn/?"
    get_url = request.POST['mhurl1']
    url = target + "mhurl1=" + get_url
    print(url)
    req = requests.get(url)
    print(req)
    jsons = req.json()
    list = jsons.get('list')
    data = jsons.get('data')
    connect = {
        'message': list,
        'data':data
    }
    return render(request, 'Cartoon/cartoon_data.html', connect)

@method_decorator(csrf_exempt)
def cartoon_show(request):
    target = "http://api.pingcc.cn/?"
    get_url = request.POST['mhurl2']
    url = target + "mhurl2=" + get_url
    print(url)
    req = requests.get(url)
    print(req)
    jsons = req.json()
    list = jsons.get('list')
    connect = {
        'message': list,
    }
    return render(request, 'Cartoon/cartoon_show.html', connect)
    # return HttpResponse(list)