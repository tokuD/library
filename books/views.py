from django.shortcuts import render
from django.views import generic
from .models import Book
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
