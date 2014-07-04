
from django.conf.urls import patterns, url
from firststep import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^nha-dat-can-ban/$', views.houseForSaleList, name='hfs_list'),
                       # url(r'^$', views.houseForSaleList, name='hfs_list'),
                       # url(r'^(?P<ja_id>\d+)/detail/$', views.detail, name='detail'),
                       )
