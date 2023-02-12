from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Event
        fields = [
            'id',
            'category',
            'category_name',
            'title',
            'description',
            'date',
            'authenticated_user_capacity',
            'authenticated_user_price',
            'anonymous_user_capacity',
            'anonymous_user_price',

        ]
