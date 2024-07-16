from django.http import HttpResponseForbidden, HttpRequest


def admin_login_required(func):
    """Decorator for check if user is admin"""

    def wrapper(request: HttpRequest, *args, **kwargs):
        """
        The func is get from HttpRequest data about current
        user and if it is not admin return HttpResponseForbidden"""
        user = request.user
        if user.is_staff or user.is_superuser:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to view this page.")

    return wrapper
