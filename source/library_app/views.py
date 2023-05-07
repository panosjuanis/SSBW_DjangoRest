from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from datetime import datetime
from . import models
from .forms import BookDetailsForm
from .models import Book

import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "library_app/home.html")


def result(request):
    if request.method == 'POST':
        search_term = request.POST.get('book_name', '')
        books = Book.objects.filter(title__icontains=search_term)
        book_data = [{'isbn': book.isbn, 'title': book.title, 'author': book.author, 'publisher': book.publisher} for book in books]
        return JsonResponse({'books': book_data})

    # If this is a GET request, render the page with the existing data
    search_term = request.GET.get('book_name', '')
    books = Book.objects.filter(title__icontains=search_term)
    return render(request, "library_app/result.html", {"books": books})
    # search = request.POST.get("book_name", "")
    # logger.info(f'Searching for books with title containing: {search}')
    # books = models.Book.objects(title__icontains=search)

    # return render(request, "library_app/result.html", {'books': books})

def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        logger.info(f'Add post petition recieved, adding new book...')
        # create a form instance and populate it with data from the request:
        form = BookDetailsForm(request.POST)
        book = models.Book()
        # check whether it's valid:
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.genre = form.cleaned_data['genre']
            book.description = form.cleaned_data['description']
            book.isbn = form.cleaned_data['isbn']
            book.image = form.cleaned_data['image']
            book.published = form.cleaned_data['published']
            book.publisher = form.cleaned_data['publisher']
            book.save()
            logger.info(f'Added the new book!')
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookDetailsForm()

    return render(request, 'library_app/add.html', {'form': form})

def details(request, book_isbn):
    logger.info(f'Retrieving book with isbn {book_isbn}... of type {type(book_isbn)}')
    book = models.Book.objects.get(isbn=book_isbn)
    
    form = BookDetailsForm()
    logger.debug(f'Form attr: {form.fields.__dir__()}')
    # populate the form with the book object
    form.fields['title'].initial = book.title
    form.fields['author'].initial = book.author
    form.fields['genre'].initial = book.genre
    form.fields['description'].initial = book.description
    form.fields['image'].initial = book.image
    form.fields['isbn'].initial = book.isbn
    form.fields['published'].initial = book.published
    form.fields['publisher'].initial = book.publisher

    context = {'form': form, 'book':book}
    return render(request, 'library_app/details.html', context)

def delete_book(request, book_isbn):
    logger.info(f'Deleting book with isbn {book_isbn}... of type {type(book_isbn)}')
    book = models.Book.objects.get(isbn=book_isbn)
    book.delete()

    logger.info(f'Deleted book with isbn {book_isbn}!')
    return HttpResponseRedirect('/search/')

def modify(request):
    book_isbn = request.POST.get("isbn", "")
    logger.info(f'Modifying book with isbn {book_isbn}... of type {type(book_isbn)}')
    book = models.Book.objects.get(isbn=book_isbn)
    form = BookDetailsForm(request.POST)
    if form.is_valid():
        book.title = form.cleaned_data['title']
        book.author = form.cleaned_data['author']
        book.genre = form.cleaned_data['genre']
        book.description = form.cleaned_data['description']
        book.isbn = form.cleaned_data['isbn']
        book.image = form.cleaned_data['image']
        book.published = form.cleaned_data['published']
        book.publisher = form.cleaned_data['publisher']
        book.save()
        logger.info(f'Modified book with isbn {book_isbn}!')
        return HttpResponseRedirect('/search/')

    return render(request, 'library_app/details.html', {'form': form, 'book':book})

