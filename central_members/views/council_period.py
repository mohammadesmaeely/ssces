from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from central_members.serializers.council_period import CouncilPeriodSerializer
from central_members.models.council_period import CouncilPeriod


class CouncilPeriodReadViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CouncilPeriod.active_objects.all()
    serializer_class = CouncilPeriodSerializer
