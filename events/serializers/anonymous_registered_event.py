from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from events.models import RegisteredEvent


class AnonymousRegisteredEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredEvent
        fields = [
            'id',
            'event',
            'phone_number',
            'is_paid',
        ]
        read_only_fields = [
            'is_paid',
        ]

    def validate_phone_number(self, value):
        RegisteredEvent.active_objects.filter(user__isnull=True, is_paid=False, phone_number=value).delete()
        return value

    def validate(self, attrs):
        if attrs['event'].registered_events.filter(is_paid=True, user__isnull=True).count() >= attrs['event'].anonymous_user_capacity:
            raise serializers.ValidationError(_("capacity is complete"))
        return attrs
