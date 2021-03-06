from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^article/', include('firststep.urls', namespace="firststep")),
    url(r'^$', 'firststep.views.home', name='home'),
    url(r'^tin-tuc/$', 'firststep.views.news', name='news'),
    url(r'^lien-he$', 'firststep.views.contact', name='contact'),
    #url(r'^lien-he/$', 'firststep.views.sendMail', name='sendMail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^search/$',"firststep.views.search", name='search'),
    url(r'^(?P<cat_key>[-\w]+)/$', 'firststep.views.viewCategory', name='viewCategory'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
