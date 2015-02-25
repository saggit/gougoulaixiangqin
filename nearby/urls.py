from django.conf.urls import patterns, url

from nearby import views

urlpatterns = patterns('',
    url(r'^get-nearby-dogs/$', views.get_nearby_dogs, name='get_nearby_dogs')
)
