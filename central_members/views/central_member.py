from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from central_members.models.central_members import CentralMember
from central_members.serializers.central_member import CentralMemberSerializer


class CentralMemberReadViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CentralMember.active_objects.all()
    serializer_class = CentralMemberSerializer

    filterset_fields = [
        'council',
    ]
