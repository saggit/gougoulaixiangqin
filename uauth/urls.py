from django.conf.urls import patterns, url

from uauth import views
from uauth import phone_views

urlpatterns = patterns('',
    url(r'^weibo-login/$', views.weibo_login, name='weibo_login'),
    url(r'^get-phone-vcode/$', phone_views.get_phone_vcode, name='get_phone_vcode')
)
