from django.shortcuts import render
from django.http import HttpResponseForbidden


def post_deleted(request) -> render:
    """
    Render post deleted page
    :param request: request object
    :return: render post deleted page
    """
    if request.user.is_staff:
        context = {"title": "Post Deleted"}
        return render(request=request, template_name="blog/post_deleted.html", context=context)
    else:
        return HttpResponseForbidden()
