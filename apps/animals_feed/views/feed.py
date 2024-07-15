from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from apps.animals_crm import models


def feed(request):
    paginator = Paginator(models.AnimalCard.objects.order_by("-created_at"), 3)

    page_obj = request.GET.get("page")

    try:
        posts = paginator.page(page_obj)
    except NameError:
        posts = paginator.page(1)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"title": "Feed", "posts": posts, "page_obj": page_obj}

    return render(request=request, template_name="feed/feed.html", context=context)
