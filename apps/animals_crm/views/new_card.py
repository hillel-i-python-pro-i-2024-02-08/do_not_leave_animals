from apps.helpers import admin_login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest
from ..forms import AnimalCardForm, AnimalPhotoFormSet, AnimalCommentFormSet


@admin_login_required
def new_card(request: HttpRequest):
    if request.method == "POST":
        form = AnimalCardForm(data=request.POST)
        photos_formset = AnimalPhotoFormSet(request.POST, request.FILES)
        comments_formset = AnimalCommentFormSet(request.POST)
        if form.is_valid() and photos_formset.is_valid() and comments_formset.is_valid():
            card = form.save()
            photos_formset.instance = card
            photos_formset.save()
            comments_formset.instance = card
            comments_formset.save()

            return redirect("crm:crm")

    else:
        form = AnimalCardForm()
        photos_formset = AnimalPhotoFormSet()
        comments_formset = AnimalCommentFormSet()
    context = {
        "title": "New Card",
        "form": form,
        "photos_formset": photos_formset,
        "comments_formset": comments_formset,
    }
    return render(request=request, template_name="crm/new_card.html", context=context)
