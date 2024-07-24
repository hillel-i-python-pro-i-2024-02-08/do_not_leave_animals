from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from apps.blog.forms import PostForm
from ..tasks import save_post


def new_post(request):
    """
    Create new post to blog page
    :param request: request object
    :return: render new post page or redirect to index page with new post
    """
    if request.user.is_staff:
        context = {"title": "New Post", "form": PostForm}
        if request.method == "POST":
            save_post(request.POST, request.FILES)
            return HttpResponseRedirect("/blog/")
        elif request.method == "GET":
            return render(request=request, template_name="blog/new_post.html", context=context)
    else:
        return HttpResponseForbidden()
