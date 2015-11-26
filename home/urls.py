from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#    url(r'^$', views.base, name='base'),

#    url(r'^about/$', views.index, name='about'),
)
