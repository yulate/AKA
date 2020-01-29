from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # 留言板路由
    url(r'^message/$', views.message, name='message'),

    # 邮件发送路由
    url(r'^sendmail/$', views.sendmail, name='sendmail'),

    # 注册登录路由
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),

    # API主页路由
    url(r'^$', views.api_index, name='api_index'),

    url(r'^get_ys/$', views.get_ys, name='get_ys'),
    url(r'^get_ysurl/$', views.get_ysurl, name='get_ysurl'),

    url(r'^get_cartoon$', views.get_cartoon, name='get_cartoon'),

    url(r'^get_hm/$', views.get_hm, name='get_hm'),
    url(r'^hm_show/$', views.hm_show, name='hm_show'),
    url(r'^hm_ss/$', views.hm_ss, name='hm_ss'),

    # # 数据库操作路由
    # url(r'^test/$', views.test, name='test'),
    # url(r'^deletes/$', views.deletes, name='deletes'),
    # url(r'^adds/$', views.adds, name='adds'),

    # # 漫画页面路由
    # url(r'^get_cartoon/$', views.cartoon_index, name='search_form'),


    # 废弃路由
    # url(r'^get_download_url/$', views.get_download_url, name='get_download_url'),
    # url(r'^get_contents/$', views.get_contents, name='get_contents'),
    # url(r'^get_train/$', views.get_train, name='get_train'),
]

urlpatterns += staticfiles_urlpatterns()