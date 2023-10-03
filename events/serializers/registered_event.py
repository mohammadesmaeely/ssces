from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from events.models import RegisteredEvent


class RegisteredEventSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        old_registered_event = RegisteredEvent.active_objects.filter(
            event=attrs['event'], user=self.context['request'].user
        ).first()
        if old_registered_event:
            state = _("not paid") if old_registered_event.is_paid else _("paid")
            raise serializers.ValidationError(f'{_("you have already registered for this event")} ({_(state)})')
        if attrs['event'].registered_events.filter(is_paid=True, user__isnull=False).count() >= attrs['event'].authenticated_user_capacity:
            raise serializers.ValidationError(_("capacity is complete"))
        return attrs
