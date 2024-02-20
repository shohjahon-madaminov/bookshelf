from rest_framework import serializers

from apps.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'url', 'pages', 'isbn', 'published', 'started_time')
        
    # def create(self, validated_data):
    #     book = Book.objects.create(**validated_data)
    #     book.user = self.context.get('')