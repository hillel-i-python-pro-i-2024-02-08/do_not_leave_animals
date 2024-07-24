from django.shortcuts import render

from apps.animals_crm import models


def card(request, card_id):
    # animal = get_object_or_404(models.AnimalCard, pk=card_id)
    animal = models.AnimalCard.objects.get(pk=card_id)
    animal_photo = animal.photos.order_by("-modified_at")
    animal_comment = models.AnimalComment.objects.filter(animal=animal).order_by("-created_at")
    context = {"title": "temp", "animal": animal, "animal_photo": animal_photo, "comments": animal_comment}

    return render(request=request, template_name="feed/card.html", context=context)
