from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from gallery.models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'is_deleted',
        'description',
    ]

    list_filter = [
        'is_deleted',
    ]

    search_fields = [
        'description',
    ]
