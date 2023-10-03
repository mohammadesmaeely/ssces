from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from core.admin import CustomDateRangeFilter
from events.models.registered_event import RegisteredEvent


class RegisteredEventModelResource(resources.ModelResource):
    class Meta:
        model = RegisteredEvent
        fields = [
            'id',
            'event__id',
            'event__title',
            'phone_number',
            'user__student_id',
            'is_paid',
        ]


@admin.register(RegisteredEvent)
class RegisteredEventAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    resource_class = RegisteredEventModelResource
    list_display = [
        'id',
        'event',
        'user',
        'phone_number',
        'is_paid',
    ]

    list_filter = [
        'is_paid',
        AutocompleteFilterFactory(_("event"), 'event',  use_pk_exact=True),
        AutocompleteFilterFactory(_("user"), 'user',  use_pk_exact=True),
        ('created_at', CustomDateRangeFilter),
    ]

    search_fields = [
        'phone_number',
        'user__student_id',
        'event__title',
    ]
