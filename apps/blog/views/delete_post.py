from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from ..models import Post


def delete_post(request, post_id):
    """
    Delete a post
    :param request: request object
    :param post_id: post id
    :return: redirect or render page
    """
    if request.user.is_staff:
        post = Post.objects.get(id=post_id)

        if request.method == "POST":
            post.delete()
            return redirect("blog:post_deleted")
        else:
            return render(
                request=request, template_name="blog/delete_post.html", context={"post": post, "title": "Delete Post"}
            )
    else:
        return HttpResponseForbidden()
