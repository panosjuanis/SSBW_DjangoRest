from django.urls import path
from library_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("result/", views.result, name="result"),
    path("add/", views.add, name="add"),
    path("details/<book_isbn>", views.details, name="details"),
    path("delete/<book_isbn>", views.delete_book, name="delete_book"),
    path("modify/", views.modify, name="modify"),
]

