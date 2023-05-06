from django.urls import path
from library_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("result/", views.result, name="result"),
]