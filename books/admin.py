from django.contrib import admin

from books.models import Book, Author, Number


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    pass


