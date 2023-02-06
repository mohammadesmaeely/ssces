from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from events.models.event_category import EventCategory


@admin.register(EventCategory)
class EventCategoryAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'name',
        'ordering_in_list',
    ]

    search_fields = [
        'id',
        'name',
        'ordering_in_list',
    ]
