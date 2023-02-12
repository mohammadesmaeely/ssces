from rest_framework import serializers

from events.models import EventCategory


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = [
            'id',
            'name',
        ]
