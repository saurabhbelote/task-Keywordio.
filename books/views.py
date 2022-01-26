import imp
from django.views.generic import ListView
from .models import Book
# Create your views here.

class BooksList(ListView):
    model = Book
    template_name = "books/index.html"