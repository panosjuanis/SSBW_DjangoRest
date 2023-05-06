from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from datetime import datetime
from . import models

def home(request):
    return render(request, "library_app/home.html")

def about(request):
    return render(request, "library_app/about.html")

def contact(request):
    return render(request, "library_app/contact.html")

def hello_there(request, name):
    return render(
        request,
        'library_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Add this code elsewhere in the file:
def search(request):

    
    return render(request, "library_app/search.html")

def result(request):
    search = request.POST.get("search", "")
    print("Searching by parameter: " + search)
    books = models.Book.objects(title__icontains=search)

    return render(request, "library_app/result.html", {'books': books})