from django.shortcuts import render


def post_deleted(request) -> render:
    """
    Render post deleted page
    :param request: request object
    :return: render post deleted page
    """
    return render(request, 'blog/post_deleted.html')
