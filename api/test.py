import requests
import json
import re


import os

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(os.path.join(BASE_DIR, 'templates'))
print(os.path.join(BASE_DIR, 'static'))

print(staticfiles_urlpatterns())

# target = "http://api.pingcc.cn/?"
# name = "ysname=复仇者联盟"
# url1 = target + name
# print(url1)
# req = requests.get(url1)
# print(req.text)
#
# a = req.json()
# print(a)
#
# res = a.get("list")
# print(res)
# for js in res:
#     print(js)
#

