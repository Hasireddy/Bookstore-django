from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse

from . models import Book

# Create your views here.

def home_view(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,"books/home.html",context)


def book_detail(request,id):
    #book = Book.objects.get(id=id)
    book = get_object_or_404(Book, id=id)
    context = {'book':book}
    return render(request,"books/book-detail.html",context)


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
