from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.

from .models import Book, Author
from .forms import AuthorForm,BookForm
# def createBook(request):
#
#     books=Book.objects.all()
#
#
#     if request.method== 'POST':
#
#         title=request.POST.get('title')
#         price=request.POST.get('price')
#
#         book=Book(title=title,price=price)
#         book.save()
#
#     return render(request, 'book.html',{'books':books})

def listBook(requst):

    books=Book.objects.all()
    paginator=Paginator(books, 4)
    page_number=requst.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(requst,'admin/listbook.html',{'books':books, 'page':page})


def detailsView(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'admin/detailsview.html',{'book':book})



def updateView(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)  # Corrected typo

        if form.is_valid():
            form.save()
            return redirect('/')  # Or use a named URL like 'list_book'

    else:
        form = BookForm(instance=book)

    return render(request, 'admin/updateview.html', {'form': form, 'book': book})


def deleteView(request,book_id):


    book=Book.objects.get(id=book_id)


    if request.method== 'POST':

        book.delete()
        return redirect('/')

    return render(request,'admin/deleteview.html',{'book':book})

def createBook(request):

    books=Book.objects.all()
    #
    if request.method=='POST':
        form=BookForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            form.save()

            return redirect('/')


    else:
        form=BookForm()



    return render(request,'admin/book.html', {'form': form,'books': books})

def Create_Author(request):

    if request.method=='POST':
        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()


            return redirect('/')

    else:
        form=AuthorForm()
    return render(request,'admin/author.html',{'form':form})


def index(request):
    return render(request,'admin/base.html')




def Search_Book(request):
    query = None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books=[]

    context={
        'books':books,
        'query':query
        # 'authors':[]
    }
    return  render(request, 'admin/search.html',context)


# def Search_Author(request):
#     query = None
#     authors = None
#
#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         authors = Author.objects.filter(Q(name__icontains=query))
#     else:
#         authors = []
#
#     context = {
#         'authors': authors,
#         'query': query
#         # 'books': []  # Pass an empty list to avoid errors in the template
#     }
#     return render(request, 'admin/search_author.html', context)

def Register_user(request):
    if request.method =='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('First_Name')
        last_name=request.POST.get('Last_Name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        c_password=request.POST.get('password1')

        if password == c_password:
            if User.objects.filter(username=username).exist():
                messages.info(request,'This is username already exist')
                return redirect('register')
            if User.objects.filter(email=email).exist():
                messages.info(request,'This is mail ID already taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email, password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request, 'This is password not matching')
            return redirect('register')

    return  render(request,'admin/register.html')


def loginUser(request):
    if request.method=='POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user=auth.authenticate(username=username,password=password)


         if user is  not None:
             auth.login(request,user)
             return redirect('home')
         else:
             messages.info(request,'please provide correct details')
             return redirect('login')

    return render(request,'admin/login.html')


def logOut(request):
    auth.logout(request)
    return redirect('login')


def homePage(request):
    return render(request,'admin/home.html')