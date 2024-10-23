from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("",views.home_view,name="home"),
    path("book-detail/<str:id>/",views.book_detail,name="book-detail"),
    path("add-book/",views.add_book,name="add-book"),
    path('edit-book/<str:id>/', views.edit_book, name='edit-book'),
    path('delete-book/<str:id>/', views.delete_book, name='delete-book'),
    ]