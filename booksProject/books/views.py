from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse

from . models import Book

from .forms import EditBookForm

# Create your views here.

def home_view(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,"books/home.html",context)





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



def book_detail(request,id):
    #book = Book.objects.get(id=id)
    book = get_object_or_404(Book, id=id)
    context = {'book':book}
    return render(request,"books/book-detail.html",context)
    


def edit_book(request,id):
    # getting the book with id to be updated
    book = Book.objects.get(id=id)
    # populating the form with the book's information
    form = EditBookForm(instance=book)
    
    if request.method == "POST":
        form = EditBookForm(request.POST,request.Files,instance=book)
          # checking if the form's data is valid
        if form.is_valid():
             # saving the data to the database
            form.save()
            return redirect("books:home")
    return render(request,"books/update-book.html",{'edit_form':form})
            
        




def delete_book(request,id):
    return HttpResponse("Book deleted")
