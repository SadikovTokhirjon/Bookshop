from django.contrib import admin
from .models import Book,Author,BookAuthor,BookReview
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title','isbn')
    list_display = ['title','isbn','description']

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('firts_name','last_name')
    list_display = ['first_name','last_name','email']


class BookAuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
