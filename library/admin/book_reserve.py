from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from simple_history.admin import SimpleHistoryAdmin

from library.models import BookReserve


@admin.register(BookReserve)
class BookReserveAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'book',
        'user',
        'reserve_date',
        'has_been_returned',
    ]

    list_filter = [
        AutocompleteFilterFactory(_("user"), 'user', use_pk_exact=True),
        AutocompleteFilterFactory(_("book"), 'book', use_pk_exact=True),
        'has_been_returned',
        'reserve_date',
    ]


