from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from central_members.models.council_period import CouncilPeriod


@admin.register(CouncilPeriod)
class CouncilPeriodAdmin(SimpleHistoryAdmin):
    list_display = [
        'id',
        'period',
    ]



