from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from cooperation.serializers.cooperation_form import CooperationFormSerializer
from cooperation.models.cooperation_form import CooperationForm


class CooperationFormReadViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = CooperationForm.active_objects.filter(show_on_site=True)
    serializer_class = CooperationFormSerializer
