from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max, F, Case, When
from django.shortcuts import render

from apps.animals_crm import models


def feed(request):
    animal_cards = models.AnimalCard.objects.annotate(
        last_comment_date=Max("comments__created_at"),
        last_update_date=Case(
            When(last_comment_date__isnull=True, then=F("modified_at")), default=F("last_comment_date")
        ),
    ).order_by("-last_update_date", "-modified_at")

    paginator = Paginator(animal_cards, 3)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    try:
        posts = paginator.page(page)
    except NameError:
        posts = paginator.page(1)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"title": "Feed", "posts": posts, "page_obj": page_obj}

    return render(request=request, template_name="feed/feed.html", context=context)
