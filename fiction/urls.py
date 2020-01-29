from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='fiction_index'),
    url(r'^get_fiction$', views.get_fiction, name='get_fiction'),
    url(r'^fiction_data/$', views.fiction_data, name='fiction_data'),
    url(r'^fiction_show/$', views.fiction_show, name='fiction_show'),
]