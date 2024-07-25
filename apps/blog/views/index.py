from django.shortcuts import render

from apps.helpers.get_page_obj import get_page_obj
from apps.blog.models import Post


def index(request):
    """
    Blog main index page
    :param request: request object
    :return: render index page
    """
    page_obj, posts = get_page_obj(request, Post.objects.order_by("-date"), 3)

    context = {"title": "Blog", "posts": posts, "page_obj": page_obj, "is_staff": request.user.is_staff}

    return render(request, "blog/index.html", context)
