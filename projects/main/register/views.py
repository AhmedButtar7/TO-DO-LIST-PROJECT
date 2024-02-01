from django.shortcuts import render, redirect
from .forms import Registerform


# Create your views here.
def register(response):
    if response.method == "POST":
        form = Registerform(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = Registerform()
    return render(response, "register/register.html", {"form": form})
