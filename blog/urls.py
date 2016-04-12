from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^about/$', views.about, name='about'),
#    url(r'^$', views.blog, name='blog'),
    url(r'^$', views.news, name='news'),
    url(r'^listing/$', views.listing, name='listing'),

#    url(r'^(?P<blog_id>\d+)/$', views.post_detail(), name='blogpost'),

    url(r'^post/new/', views.post_new, name='post_new'),
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^login/$', views.LoginFormView.as_view()),
#    url(r'^redirect/$', views.post_redirect),
)
