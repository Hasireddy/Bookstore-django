from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("",views.home_view,name="home"),
    path("book-detail/<int:id>/",views.book_detail,name="book-detail"),
    path("add-book/",views.add_book,name="add-book"),
    path('edit-book/<int:id>/', views.edit_book, name='edit-book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete-book'),
    ]

