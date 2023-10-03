from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
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
        AutocompleteFilterFactory(_("user"), 'user', use_pk_exact=True),
    ]

    search_fields = [
        'text',
        'phone_number',
        'email',
    ]
