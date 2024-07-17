from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from apps.helpers import admin_login_required
from ..models import AnimalCard


@admin_login_required
def delete_card(request: HttpRequest, card_id: int):
    card_instance: AnimalCard = get_object_or_404(AnimalCard, pk=card_id)
    if request.method == "POST":
        card_instance.delete()
        return redirect("crm:crm")

    else:
        context: dict = {"title": "Confirm delete", "instance": card_instance}
        return render(request=request, template_name="crm/confirm_delete.html", context=context)
