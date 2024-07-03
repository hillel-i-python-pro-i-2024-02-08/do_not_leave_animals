from django.shortcuts import render
from django.http import HttpResponseRedirect

from ..models import Post
from ..forms import PostForm


def index(request):
    last_posts = Post.objects.order_by('-date')[:5]
    context = {"title": "Blog", "posts": last_posts}

    return render(request=request,
                  template_name='blog/index.html',
                  context=context)


def new_post(request):
    context = {"title": "New Post", "form": PostForm}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/")
    elif request.method == 'GET':
        return render(request=request,
                      template_name='blog/new_post.html',
                      context=context)
