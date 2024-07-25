from django.shortcuts import render

from apps.helpers.get_page_obj import get_page_obj
from apps.animals_crm import models


def feed(request):
    animal_cards = models.AnimalCard.objects.order_by("-modified_at")

    page_obj, posts = get_page_obj(request, animal_cards, 3)

    context = {"title": "Feed", "posts": posts, "page_obj": page_obj}

    return render(request=request, template_name="feed/feed.html", context=context)
