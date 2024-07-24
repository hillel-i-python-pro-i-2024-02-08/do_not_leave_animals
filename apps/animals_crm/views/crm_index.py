from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.helpers import admin_login_required

from ..models import AnimalCard


@admin_login_required
def crm_index(request):
    """
    Crm main index page
    :param request: request object
    :return: render index page
    """
    paginator = Paginator(AnimalCard.objects.order_by("-modified_at"), 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    try:
        animals = paginator.page(page)
    except NameError:
        animals = paginator.page(1)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {"title": "CRM", "animals": animals, "page_obj": page_obj}

    return render(request, "crm/crm.html", context)
