from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Post


def index(request):
    """
    Blog main index page
    :param request: request object
    :return: render index page
    """
    paginator = Paginator(Post.objects.order_by("-date"), 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        posts = paginator.page(page)
    except NameError:
        posts = paginator.page(1)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"title": "Blog", "posts": posts, "page_obj": page_obj, "is_staff": request.user.is_staff}

    return render(request, "blog/index.html", context)

