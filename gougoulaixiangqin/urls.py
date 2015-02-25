from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gougoulaixiangqin.views.home', name='home'),
    url(r'^uauth/', include('uauth.urls')),
    url(r'^gougou/', include('gougou.urls')),
    url(r'^nearby/', include('nearby.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
