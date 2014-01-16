from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL
from blog.models import Post, User, Category, Tag, Comment


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'

class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = 'tag'

class PostResource(ModelResource):
	author = fields.ForeignKey(UserResource, 'author', full=True)
	categories = fields.ToManyField(CategoryResource, 'categories', full=True)
	tags = fields.ToManyField(TagResource, 'tags', full=True)
    	class Meta:
            queryset = Post.objects.all().order_by("-pub_date") #ordena recientes
            resource_name = 'post'
            limit = 20 #limita a 20 ultimos posts
            filtering = {'tags': ALL, 'categories': ALL}
            # ?tags=1&format=json , ?categories=1&format=json

class CommentResource(ModelResource):
	post = fields.ForeignKey(PostResource, 'post')
    	class Meta:
        	queryset = Comment.objects.all()
        	resource_name = 'comment'

        
