from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from cooperation.models.cooperation_reply import CooperationReply


@admin.register(CooperationReply)
class CooperationReplyAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'cooperation',
        'user',
    ]

    list_filter = [
        'cooperation',
    ]

    search_fields = [
        'text',
        'phone_number',
        'email',
    ]
