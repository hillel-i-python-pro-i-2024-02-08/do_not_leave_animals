from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.blog.forms import PostForm


def new_post(request):
    """
    Create new post to blog page
    :param request: request object
    :return: render new post page or redirect to index page with new post
    """
    context = {"title": "New Post", "form": PostForm}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/")
    elif request.method == 'GET':
        return render(request=request,
                      template_name='blog/new_post.html',
                      context=context)
