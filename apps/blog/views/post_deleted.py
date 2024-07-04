from django.shortcuts import render


def post_deleted(request) -> render:
    """
    Render post deleted page
    :param request: request object
    :return: render post deleted page
    """
    context = {"title": "Post Deleted"}
    return render(request=request,
                  template_name='blog/post_deleted.html',
                  context=context)
