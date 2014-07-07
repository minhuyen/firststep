from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^article/', include('firststep.urls', namespace="firststep")),
    url(r'^$', 'firststep.views.home', name='home'),
    url(r'^news/$', 'firststep.views.houseForSaleList', name='houseForSale'),
    url(r'^news/$', 'firststep.views.houseForRentList', name='houseForRent'),
    url(r'^news/$', 'firststep.views.coastalVillaList', name='coastalVilla'),
    url(r'^news/$', 'firststep.views.apartmentList', name='apartment'),
    url(r'^news/$', 'firststep.views.projectLandList', name='projectLand'),
    url(r'^lien-he$', 'firststep.views.contact', name='contact'),
    url(r'^haha/$', 'firststep.views.sendMail', name='sendMail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
