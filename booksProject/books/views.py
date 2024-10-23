from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("Home page")

def book_detail(request,id):
    return HttpResponse("Book detail")

def add_book(request):
    return HttpResponse("Book added")

def edit_book(request,id):
    return HttpResponse("Book edited")

def delete_book(request,id):
    return HttpResponse("Book deleted")
