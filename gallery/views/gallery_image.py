from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from gallery.models import GalleryImage
from gallery.serializers.gallery_image import GalleryImageSerializer


class GalleryImageReadViewSet(ReadOnlyModelViewSet):
    queryset = GalleryImage.active_objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [AllowAny]
