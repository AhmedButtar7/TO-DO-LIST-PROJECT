from django.urls import path
from . import views
#here is the urls of project1 application
urlpatterns = [
    path('', views.register, name = "register")
]