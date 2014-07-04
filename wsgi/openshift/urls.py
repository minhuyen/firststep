from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'views.home', name='home'),
    # url(r'^firststep/', include('firststep.urls', namespace="firststep")),
    url(r'^$', include('firststep.urls', namespace="firststep")),
    url(r'^$', 'firststep.views.home', name='home'),
    url(r'^nha-dat-can-ban$', 'firststep.views.house', name='house'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
