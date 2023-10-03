from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    authenticated_user_registered_count = serializers.SerializerMethodField()
    anonymous_user_registered_count = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = [
            'id',
            'category',
            'category_name',
            'title',
            'image',
            'description',
            'date',
            'authenticated_user_capacity',
            'authenticated_user_price',
            'anonymous_user_capacity',
            'anonymous_user_price',
            'authenticated_user_registered_count',
            'anonymous_user_registered_count',
        ]

    def get_authenticated_user_registered_count(self, instance):
        return instance.registered_events.filter(user__isnull=False, is_paid=True).count()

    def get_anonymous_user_registered_count(self, instance):
        return instance.registered_events.filter(user__isnull=True, is_paid=True).count()

