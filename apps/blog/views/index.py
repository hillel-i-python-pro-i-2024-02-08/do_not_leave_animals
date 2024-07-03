from django.shortcuts import render
from ..models import Post


def index(request):
    # last_posts = Post.objects.order_by('-created_at')[:5]
    last_posts = Post.objects.order_by('-date')[:3]

    context = {"title": "Blog", "posts": last_posts}
    return render(request=request,
                  template_name='blog/index.html',
                  context=context)


def new_post(request):
    context = {"title": "New Post"}
    if request.method == "POST":
        ...
    if request.method == 'GET':
        return render(request=request,
                      template_name='blog/new_post.html')
