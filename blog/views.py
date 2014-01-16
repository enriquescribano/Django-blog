from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, render_to_response

from blog.models import Post, Category, Tag, Comment

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:25]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    allcomments = Comment.objects.filter(post = post_id)
    return render(request, 'blog/post_view.html', {'post': post, 'allcomments': allcomments})

def post_category (request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	latest_post_list_with_category = Post.objects.filter(categories = category_id)[:10]
	return render(request, 'blog/post_category.html', {'category': category, 'latest_post_list_with_category': latest_post_list_with_category})

def post_tag (request, tag_id):
	tag = get_object_or_404(Tag, pk=tag_id)
	latest_post_list_with_tag = Post.objects.filter(tags = tag_id)[:10]
	return render(request, 'blog/post_tag.html', {'tag': tag, 'latest_post_list_with_tag': latest_post_list_with_tag})