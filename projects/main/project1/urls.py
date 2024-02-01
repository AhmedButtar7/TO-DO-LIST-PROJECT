from django.urls import path
from . import views
#here is the urls of project1 application
urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.create, name="index"),
path("<int:id>", views.index, name="index"),

path("view/", views.view, name="view"),
]