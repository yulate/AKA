import re
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'fiction/fiction_index.html')

def get_fiction(request):
    target = "http://api.pingcc.cn/?"
    if request.POST:
        xsname = "xsname=" + request.POST['xsname']
        urls = target + xsname
        req = requests.get(urls)
        a = req.json()
        res = a.get('list')
        print(res)
        connect = {
            'context': res
        }
    return render(request, 'fiction/fiction_list.html', connect)


@method_decorator(csrf_exempt)
def fiction_data(request):
    target = "http://api.pingcc.cn/?"
    if request.POST:
        get_url = request.POST['xsurl1']
        url = target + "xsurl1=" + get_url
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
    if request.GET:
        get_url = request.GET.get('xsurl1')
        url = target + "xsurl1=" + get_url
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
    return render(request, 'fiction/fiction_data.html', connect)

@method_decorator(csrf_exempt)
def fiction_show(request):
    target = "http://api.pingcc.cn/?"
    if request.POST:
        get_url = request.POST['xsurl2']
        url = target + "xsurl2=" + get_url
        print(url)
        req = requests.get(url)
        print(req)
        jsons = req.json()
        list = str(jsons.get('content'))
        lists = list.replace('\'' , '<br>')
        listss = lists.replace('\\xa0', '')
        num = jsons.get('num')
        connect = {
            'message': listss,
            'num':num
        }
    return render(request, 'fiction/fiction_show.html', connect)
    # return HttpResponse(lists)