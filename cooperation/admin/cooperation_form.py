from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from cooperation.models.cooperation_form import CooperationForm


@admin.register(CooperationForm)
class CooperationFormAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'title',
        'show_on_site',
    ]

    list_filter = [
        'show_on_site',
    ]

    search_fields = [
        'id',
        'title',
        'description',
    ]
