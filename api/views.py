from rest_framework import generics
from django.shortcuts import render
from Books.models import Book
from .serializers import BookSerializers, TodoSerializers
from todo.models import Todo
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class  = BookSerializers

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoListDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers