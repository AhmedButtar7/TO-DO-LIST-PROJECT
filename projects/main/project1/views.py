from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDOList, Item
from .forms import CreateNewList


# Create your views here.
def index(response, id):
    ls = ToDOList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    return render(response, "project1/list.html", {"ls":ls})

def home(response):
    return render(response, "project1/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = to
            response.User.todolist_set.create(name= n)

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "project1/create.html", {"form":form})

def view(response):
    return render(response, project1/view.html, {})
