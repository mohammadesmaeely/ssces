from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from events.forms.event import EventAdminForm
from events.models.event import Event


@admin.register(Event)
class EventAdmin(SimpleHistoryAdmin):
    form = EventAdminForm

    list_display = [
        'id',
        'category',
        'title',
        'date',
        'authenticated_user_capacity',
        'authenticated_user_price',
        'anonymous_user_capacity',
        'anonymous_user_price',
        'show_on_site',
    ]

    list_filter = [
        'category',
        'show_on_site',
    ]

    search_fields = [
        'id',
        'title',
        'description',
    ]
