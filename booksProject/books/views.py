from django.shortcuts import render,redirect

from django.http import HttpResponse

from . models import Book

# Create your views here.

def home_view(request):
    return HttpResponse("Home page")

def book_detail(request,id):
    return HttpResponse("Book detail")

def add_book(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image_file')
        #creating and saving the book
        book = Book.objects.create(
            title = data['title'],
            author = data['author'],
           isbn = data['isbn'],
           price = data['price'],
           image = image     
        )
        return redirect("books:home")
    return render(request,"books/add-book.html")
    


def edit_book(request,id):
    return HttpResponse("Book edited")

def delete_book(request,id):
    return HttpResponse("Book deleted")
