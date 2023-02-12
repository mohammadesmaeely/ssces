from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from events.serializers.event_categroy import EventCategorySerializer
from events.models.event_category import EventCategory



class EventCategoryReadViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = EventCategory.active_objects.all()
    serializer_class = EventCategorySerializer
