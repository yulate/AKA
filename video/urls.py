from django.conf.urls import url
from . import views

urlpatterns = [
    # 影视页面路由
    url(r'^$', views.search_form, name='search_form'),
    # url(r'^search/$', views.search, name='search'),
    url(r'^get_yss$', views.get_yss, name='get_yss'),
    url(r'^video/$', views.video, name='video'),
    url(r'^series/$', views.series, name='series'),
]