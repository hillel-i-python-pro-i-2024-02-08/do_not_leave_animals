from django.shortcuts import render
from apps.helpers import admin_login_required
from apps.helpers.get_page_obj import get_page_obj

from ..models import AnimalCard


@admin_login_required
def crm_index(request):
    """
    Crm main index page
    :param request: request object
    :return: render index page
    """
    page_obj, posts = get_page_obj(request, AnimalCard.objects.order_by("-modified_at"), 10)

    context = {"title": "CRM", "animals": posts, "page_obj": page_obj}

    return render(request, "crm/crm.html", context)
