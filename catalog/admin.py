from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Image


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date','display_genre')




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')


#admin.site.register(Genre)
#admin.site.register(Image)

