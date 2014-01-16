from django.contrib import admin

from blog.models import User, Comment, Post, Category, Tag

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Tag)
