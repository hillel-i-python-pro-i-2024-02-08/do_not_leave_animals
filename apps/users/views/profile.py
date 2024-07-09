from django.shortcuts import render


def profile(request):
    user = request.user
    context = {"title": user.username, "user": user}

    return render(request=request, template_name="users/profile.html", context=context)
