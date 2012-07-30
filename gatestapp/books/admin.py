
from django.contrib import admin
from models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date',)
    search_fields = ('title',)
    list_filter = ('publication_date',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website',)
    search_fields = ('name',)
    list_filter = ('city', 'state_province', 'country',)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
