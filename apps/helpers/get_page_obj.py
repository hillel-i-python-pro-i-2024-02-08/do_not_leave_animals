from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_page_obj(request, query, count):
    paginator = Paginator(query, count)
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
    return page_obj, posts
