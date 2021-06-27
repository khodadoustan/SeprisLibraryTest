from django.contrib import admin

from .models import Book, Publisher, Writer


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['user', 'name', 'phone', 'address']
    list_display = ['pk', 'user', 'name', 'phone', 'address', 'creation_date']
    search_fields = ('name',)


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    fields = ['user', 'first_name', 'last_name', 'sure_name']
    list_display = ['pk', 'first_name', 'last_name', 'sure_name', 'creation_date']
    search_fields = ('first_name', 'last_name', 'sure_name')


class WriterInline(admin.TabularInline):
    model = Book.writers.through
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['user', 'title', 'pages', 'publish_year', 'publisher']
    list_display = ['pk', 'title', 'pages', 'publish_year', 'publisher', 'creation_date']
    inlines = [WriterInline]
    search_fields = ('title',)
    list_filter = ('writers', 'publisher')
