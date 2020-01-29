import json
import re

import requests
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from lxml import etree

from .forms import Api_messageFrom, Api_userForm
from .models import Api_message, Api_user, UV
from .cartoons import gufengmh, comic


# Create your views here.
def api_index(request):
    return render(request, 'api/api_index.html')


@csrf_exempt
def message(request):
    if request.method != 'POST':
        message_list = Api_message.objects.order_by('-data_added')
        form = Api_messageFrom()
        context = {'message_list': message_list, 'form': form}
        return render(request, 'api/message.html', context)
    form = Api_messageFrom(data=request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('api:message'))


def sendmail(request):
    '''
    请求方式：get
    请求参数：1. title=主题
             2. content=内容
             3. from=发件人邮箱
             4. to=收件人邮箱
    请求实例：http://127.0.0.1:8000/api/sendmail/?title=主题&content=内容&from=yfhadmin@163.com&to=2113778814@qq.com
    '''
    title = request.GET.get('title')
    content = request.GET.get('content')
    api_from = request.GET.get('from')
    to = request.GET.get('to')
    send_mail(title, content, api_from,
              [to], fail_silently=False)
    a = '你已经成功给' + to + '发送了一封邮件，内容为：' + content
    return HttpResponse(a)


def register(request):
    '''
    请求方式：get
    请求参数：1. username=用户名
             2. password=密码
             3. vip=是否vip
             4. score=初始积分
    请求实例：http://127.0.0.1:8000/api/register/?username=user1&password=123456&vip=False&score=100
    '''
    username = request.GET.get('username')
    temp = Api_user.objects.all()
    for i in temp:
        if username == i.username:
            return HttpResponse('[失败]该用户名已被注册')
    password = request.GET.get('password')
    vip = request.GET.get('vip')
    score = request.GET.get('score')
    form = Api_userForm(data=request.GET)
    if form.is_valid():
        form.save()
    return HttpResponse('[成功]恭喜你注册成功!')


def login(request):
    '''
    请求方式：get
    请求参数：1. username = 用户名
             2. password = 密码
    请求实例：http://127.0.0.1:8000/api/login/?username=user1&password=123456
    '''
    login_uname = request.GET.get('username')
    login_pwd = request.GET.get('password')
    names_pwd = Api_user.objects.all()
    for temp in names_pwd:
        if login_uname == temp.username and login_pwd == temp.password:
            return HttpResponse('[成功]登陆成功')
        else:
            return HttpResponse('[失败]账号或密码错误')


def get_ys(request):
    '''
    java请求接口：
        请求方式：get
        请求参数：1. name = 电影名称
        请求实例：http://127.0.0.1:8000/api/get_ys/?name=德鲁大叔
    '''
    target = "http://api.pingcc.cn/?"
    name = "ysname=" + request.GET.get('name')
    url1 = target + name
    print(url1)
    req = requests.get(url1)
    a = req.json()
    res = a.get('list')
    print(res)
    return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")


def get_ysurl(request):
    '''
    java请求接口：
        请求方式：get
        请求参数：1. ysurl = 使用get_ys所获取到的url
        请求实例：http://127.0.0.1:8000/api/get_ysutl/?ysurl=okvod-detail-id-19874.html
    '''
    target = "http://api.pingcc.cn/?"
    get_url = request.GET.get('ysurl')
    # json1 = json.loads(get_url)
    # url2 = json1.get('url')
    # print(url2)
    url = target + "ysurl=" + get_url
    print(url)
    req = requests.get(url)
    print(req)
    jsons = req.json()
    list = jsons.get('list')
    return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json,charset=utf-8")


@method_decorator(csrf_exempt)
def get_cartoon(request):
    target = "http://api.pingcc.cn/?"
    mhname = "mhname=" + request.POST['mhname']
    urls = target + mhname
    req = requests.get(urls)
    a = req.json()
    res = a.get('list')
    return HttpResponse(res, content_type="application/json,charset=utf-8")


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
        'data': data
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


def get_hm(request):
    res = comic.get_mhname()
    # return HttpResponse(res)
    connect = {
        'new_list':res
    }
    return render(request,'api/hm/hm_new_list.html',connect)

def hm_show(request):
    url1 = request.GET.get('url1')
    res = comic.mhurl1(url1)
    # return HttpResponse(res)
    connect = {
        'list':res
    }
    return render(request,'api/hm/hm_show.html',connect)

def hm_ss(request):
    mhname = request.GET.get('mhname')
    res = comic.search_photos(mhname)
    connect = {
        'new_list' : res
    }
    # return HttpResponse(res)
    return render(request,'api/hm/hm_new_list.html',connect)

# return render(request, 'api/test.html',{'uvs':uvs})

# def get_download_url(request):
#     server = 'https://www.kanmaoxian.com/'
#     target = 'https://www.kanmaoxian.com/51/51335/index.html'
#     names = []
#     urls = []
#
#     req = requests.get(url= target)
#     html = req.text.encode('iso-8859-1').decode('gbk')
#     div_bf = BeautifulSoup(html)
#     div = div_bf.find_all('section', class_='ml_main')
#     a_bf = BeautifulSoup(str(div[0]))
#     a = a_bf.find_all('a')
#     for each in a[0:]:
#         names.append(each.string)
#         urls.append(server + each.get('href'))
#     resp = {'names':names, 'urls':urls}
#     return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json,charset=utf-8")

# def get_contents(request):
#     '''
#     请求方式：get
#     请求参数：1. urls = 请求地址
#     请求实例：http://127.0.0.1:8000/api/get_contents/?urls=https://www.kanmaoxian.com//51/51335/10445460.html
#     '''
#     target = request.GET.get('urls')
#
#     req = requests.get(url=target)
#     html = req.text.encode('iso-8859-1').decode('gbk')
#     bf = BeautifulSoup(html)
#     texts = bf.find_all('div', class_='yd_text2')
#     texts = texts[0].text.replace('\xa0' * 4, '\n')
#     return HttpResponse(texts)

# def get_train(request):
#     """
#             请求方式：get
#             请求参数：1. type = 乘坐类型
#                      2. from = 起始地点
#                      3. to = 结束地点
#                      4. date = 时间
#             请求实例：http://127.0.0.1:8000/api/get_train/?&from=北京&to=南宁&date=2019-11-11
#     """
#
#     requests.packages.urllib3.disable_warnings()
#
#     code_dict = {v:k for k, v in station.items()}
#
#     from_station_name = request.GET.get('from')
#     to_station_name = request.GET.get('to')
#     leave_time = request.GET.get('date')
#     print(from_station_name, to_station_name ,leave_time)
#     from_station = station[from_station_name]
#     to_station = station[to_station_name]
#
#     url = (
#         'https://kyfw.12306.cn/otn/leftTicket/query?'
#         'leftTicketDTO.train_date={}&'
#         'leftTicketDTO.from_station={}&'
#         'leftTicketDTO.to_station={}&'
#         'purpose_codes=ADULT'
#     ).format(leave_time, from_station, to_station)
#     print(url)
#
#     info_list = []
#     try:
#         r = requests.get(url, verify = False)
#         raw_train = r.json()['data']['result']
#
#         for raw_train in raw_train.split('|'):
#
#             data_list = raw_train.split('|')
#
#             train_no = data_list[3]
#             from_station_code = data_list[6]
#             from_station_name = code_dict[from_station_code]
#
#             to_station_code = data_list[7]
#             to_station_name = code_dict[to_station_code]
#
#             start_time = data_list[8]
#
#             arrive_time = data_list[9]
#
#             time_fucked_up = data_list[10]
#
#             first_class_seat = data_list[31] or '--'
#
#             second_class_seat = data_list[30] or '--'
#             # 软卧
#             soft_sleep = data_list[23] or '--'
#             # 硬卧
#             hard_sleep = data_list[28] or '--'
#             # 硬座
#             hard_seat = data_list[29] or '--'
#             # 无座
#             no_seat = data_list[26] or '--'
#
#             # 打印查询结果
#             info = (
#             '车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n座位情况：\n 一等座：「{}」 \n二等座：「{}」\n软卧：「{}」\n硬卧：「{}」\n硬座：「{}」\n无座：「{}」\n\n'.format(
#                 train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,
#                 second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))
#
#             info_list.append(info)
#
#         return info_list
#     except:
#         return ' 输出信息有误，请重新输入'
#
#     return HttpResponse(info_list)
