from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.books import serializers
from apps.books.models import Book


class BooksListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.BookSerializer
    
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    

class BookCreateAPIView(CreateAPIView):
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticated, )
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookUpdateAPIView(UpdateAPIView):
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookDeleteAPIView(DestroyAPIView):
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
