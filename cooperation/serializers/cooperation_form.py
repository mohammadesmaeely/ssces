from rest_framework import serializers

from cooperation.models.cooperation_form import CooperationForm


class CooperationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperationForm
        fields = [
            'id',
            'title',
            'description',
        ]
