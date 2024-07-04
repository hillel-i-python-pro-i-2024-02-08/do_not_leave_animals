from django.shortcuts import render

from ..models import Post


def index(request):
    """
    Blog index page
    :param request: request object
    :return: render index page
    """
    last_posts = Post.objects.order_by('-date')[:5]
    context = {"title": "Blog", "posts": last_posts}

    return render(request=request,
                  template_name='blog/index.html',
                  context=context)


