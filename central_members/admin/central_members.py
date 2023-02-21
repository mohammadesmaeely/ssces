from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from central_members.models.central_members import CentralMember


@admin.register(CentralMember)
class CentralMemberAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'name',
        'council',
        'phone_number',
        'user',
    ]

    list_filter = [
        'council',
    ]

    search_fields = [
        'id',
        'name',
        'phone_number',
    ]
