from rest_framework import serializers
from Books.models import Book
from todo.models import Todo
class BookSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ('id', 'Title', 'Author', 'ShelfNo')
class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'details')

