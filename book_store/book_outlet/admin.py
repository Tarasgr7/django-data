from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields=("slug",)
    list_filter=('title','rating',)
    list_display=('title','rating','author',)

admin.site.register(Book, BookAdmin)

# Register your models here.
