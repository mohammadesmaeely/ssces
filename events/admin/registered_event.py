from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from simple_history.admin import SimpleHistoryAdmin

from events.models.registered_event import RegisteredEvent


@admin.register(RegisteredEvent)
class RegisteredEventAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'event',
        'user',
        'phone_number',
        'is_paid',
    ]

    list_filter = [
        AutocompleteFilterFactory(_("event"), 'event',  use_pk_exact=True)
    ]

