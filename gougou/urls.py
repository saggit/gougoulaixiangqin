from django.conf.urls import patterns, url

from gougou import views

urlpatterns = patterns('',
    url(r'^gougou-edit/$', views.gougou_edit, name='gougou_edit'),
    url(r'^get-my-gougous/$', views.get_my_gougous, name='get_my_gougous')
)
