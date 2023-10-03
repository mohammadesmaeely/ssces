from rest_framework.permissions import AllowAny
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from events.models import RegisteredEvent
from events.serializers.anonymous_registered_event import AnonymousRegisteredEventSerializer


class AnonymousRegisteredEventView(mixins.CreateModelMixin, GenericViewSet, mixins.RetrieveModelMixin):
    permission_classes = [AllowAny]
    queryset = RegisteredEvent.active_objects.none()

    def get_queryset(self):
        return RegisteredEvent.active_objects.filter(is_paid=False, user__isnull=True)

    serializer_class = AnonymousRegisteredEventSerializer

    @action(detail=True, methods=['post'])
    def pay(self, request, pk):
        registered_event = self.get_object()
        registered_event.is_paid = True
        registered_event.save()
        return Response(
            AnonymousRegisteredEventSerializer(registered_event,  context={"request": request}).data,
            status=status.HTTP_200_OK
        )
