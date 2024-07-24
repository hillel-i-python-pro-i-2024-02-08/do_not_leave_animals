from apps.helpers import admin_login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from ..forms import AnimalCardForm, AnimalPhotoFormSet, AnimalCommentFormSet
from ..models import AnimalCard


@admin_login_required
def edit_card(request: HttpRequest, card_id: int):
    card_instance = get_object_or_404(AnimalCard, pk=card_id)
    if request.method == "POST":
        form = AnimalCardForm(data=request.POST, instance=card_instance)
        photos_formset = AnimalPhotoFormSet(request.POST, request.FILES, instance=card_instance)
        comments_formset = AnimalCommentFormSet(request.POST, instance=card_instance)
        if form.is_valid() and photos_formset.is_valid() and comments_formset.is_valid():
            form.save()
            photos_formset.save()
            comments_formset.save()
            return redirect("crm:crm")
    else:
        form = AnimalCardForm(instance=card_instance)
        photos_formset = AnimalPhotoFormSet(instance=card_instance)
        comments_formset = AnimalCommentFormSet(instance=card_instance)
    context = {
        "title": "Edit Card",
        "form": form,
        "photos_formset": photos_formset,
        "comments_formset": comments_formset,
        "actual_card": card_instance,
    }
    return render(request=request, template_name="crm/edit_card.html", context=context)
