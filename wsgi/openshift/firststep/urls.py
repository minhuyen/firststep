
from django.conf.urls import patterns, url
from firststep import views

urlpatterns = patterns('',
                       url(r'^article/(?P<ja_id>\d+)/$', views.detail, name='detail'),
                       )
