from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from library.models import Book


@admin.register(Book)
class BookAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'name',
    ]

    search_fields = [
        'name',
    ]
