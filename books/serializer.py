from rest_framework import serializers

from BookStore.settings import MEDIA_URL
from .models import Book, Category,FavoriteBooks,Author


class AuthorSerializer(serializers.ModelSerializer):
    AName = serializers.CharField(max_length=23)
    class Meta:
        model = Author
        fields = ['AName']

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    author_name = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = [ 'name', 'publisher', 'author_name', 'summery', 'rating','Year','Price','Edition', 'image', 'created_at', 'updated_at']



class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id','title','books',  'created_at', 'updated_at']

class favoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBooks
        fields = ['id', 'user', 'book']









