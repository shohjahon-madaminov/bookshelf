from django.contrib import admin

from apps.books.models import Book


class BookAmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
admin.site.register(Book, BookAmin)