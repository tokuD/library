from rest_framework import generics
from django.shortcuts import render

from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    """read-only end-point for all book instances"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
