from django.conf.urls import patterns, include, url

from blog.api import PostResource, UserResource, CategoryResource, TagResource, CommentResource
from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())
v1_api.register(CategoryResource())
v1_api.register(TagResource())
v1_api.register(CommentResource())
# v1_api.register(PostByTagResource())

urlpatterns = patterns('',
    
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(v1_api.urls)),
)
