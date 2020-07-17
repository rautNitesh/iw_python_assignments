from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    return render(request, 'blogapp/home.html')


def blog(request):
    blog_posts = Blog.objects.all()
    context = {
        "posts": blog_posts
    }
    return render(request, 'blogapp/blog.html', context)


def blog_detail(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blogapp/blog_detail.html', context)
