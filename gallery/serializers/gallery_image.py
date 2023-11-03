from rest_framework import serializers

from gallery.models import GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

