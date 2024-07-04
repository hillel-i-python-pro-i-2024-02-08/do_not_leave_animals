from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Post


def index(request):
    """
    Blog main index page
    :param request: request object
    :return: render index page
    """
    posts = Post.objects.order_by('-date')[:5]
    context = {"title": "Blog", "posts": posts}

    return render(request=request,
                  template_name='blog/index.html',
                  context=context)


def index_page(request, page_id):
    """
    Blog index page (example: /blog/page_id)
    :param request: request object
    :param page_id: page id
    :return: render index page
    """
    paginator = Paginator(Post.objects.order_by("-date"), 5)
    posts = paginator.page(page_id)
    context = {"title": "Blog", "posts": posts}

    return render(request=request,
                  template_name='blog/index.html',
                  context=context)
