from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


def register(request):
    """
    Register a new user.
    """
    if request.method != "POST":
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home_page:home")

    context = {"form": form, "title": "Register"}
    return render(request=request, template_name="registration/register.html", context=context)
