from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from events.models import RegisteredEvent
from events.serializers.registered_event import RegisteredEventSerializer


class RegisteredEventView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = RegisteredEvent.active_objects.none()

    def get_queryset(self):
        user = self.request.user
        if self.action in ['pay']:
            return RegisteredEvent.active_objects.filter(is_paid=False, user=user)
        else:
            return RegisteredEvent.active_objects.filter(user=user)

    serializer_class = RegisteredEventSerializer

    filterset_fields = [
        'event',
        'is_paid',
    ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @action(detail=True, methods=['post'])
    def pay(self, request, pk):
        registered_event = self.get_object()
        registered_event.is_paid = True
        registered_event.save()
        return Response(
            RegisteredEventSerializer(registered_event,  context={"request": request}).data,
            status=status.HTTP_200_OK
        )
