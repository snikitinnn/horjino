from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^about/$', views.about, name='about'),
    url(r'^$', views.blog, name='blog'),
)
