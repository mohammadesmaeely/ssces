from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from users.models import User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    model = User

    list_display = (
        'id',
        'username',
        'name',
        'phone_number',
        'student_id',
    )

    search_fields = (
        'id',
        'username',
        'name',
        'phone_number',
        'student_id',
    )

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()
