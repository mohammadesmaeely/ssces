from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from events.serializers.event import EventSerializer
from events.models import Event


class EventViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Event.active_objects.none()
    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_admin:
            return Event.active_objects.all()
        return Event.active_objects.filter(show_on_site=True)

    serializer_class = EventSerializer
    filterset_fields = [
        'category'
    ]
