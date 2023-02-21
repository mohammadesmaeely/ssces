from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from cooperation.models.cooperation_reply import CooperationReply
from cooperation.serializers.cooperation_reply import CooperationReplySerializer


class CooperationReplyView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CooperationReplySerializer
    queryset = CooperationReply.active_objects.none()
    def get_queryset(self):
        return CooperationReply.active_objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
