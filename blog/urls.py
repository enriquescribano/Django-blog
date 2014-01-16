from django.conf.urls import patterns, url

from blog import views
from blog.models import Post


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_view, name='post_view'),
    url(r'^category/(?P<category_id>\d+)/$', views.post_category, name='post_category'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.post_tag, name='post_tag')
)