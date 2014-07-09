from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^article/', include('firststep.urls', namespace="firststep")),
    url(r'^$', 'firststep.views.home', name='home'),
    url(r'^tin-tuc/$', 'firststep.views.news', name='news'),
    url(r'^dat-nen-du-an/$', 'firststep.views.projectLandList', name='projectLand'),
    url(r'^nha-dat-can-ban/$', 'firststep.views.houseForSaleList', name='houseForSale'),
    url(r'^nha-dat-cho-thue/$', 'firststep.views.houseForRentList', name='houseForRent'),
    url(r'^biet-thu-ven-bien/$', 'firststep.views.coastalVillaList', name='coastalVilla'),
    url(r'^can-ho/$', 'firststep.views.apartmentList', name='apartment'),
    url(r'^lien-he$', 'firststep.views.contact', name='contact'),
    url(r'^lien-he/$', 'firststep.views.sendMail', name='sendMail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
