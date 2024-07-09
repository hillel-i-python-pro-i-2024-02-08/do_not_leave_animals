from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from apps.blog.forms import PostForm
from apps.blog.models import Post


def edit_post(request, post_id):
    """
    Edit post on blog page
    :param request: request object
    :param post_id: post id
    :return: render edit post page or redirect to index page with posts
    """
    if request.user.is_staff:
        post = Post.objects.get(id=post_id)

        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/blog/")
        elif request.method == "GET":
            context = {"title": "Edit Post", "form": PostForm(instance=post), "post_id": post_id}
            return render(request=request, template_name="blog/edit_post.html", context=context)
    else:
        return HttpResponseForbidden()
