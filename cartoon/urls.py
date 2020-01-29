from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='cartoon_index'),
    url(r'^get_cartoon$', views.get_cartoon, name='get_cartoon'),
    url(r'^cartoon_data/$', views.cartoon_data, name='cartoon_data'),
    url(r'^cartoon_show/$', views.cartoon_show, name='cartoon_show'),
]