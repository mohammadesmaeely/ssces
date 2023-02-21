from rest_framework import serializers

from central_members.models.council_period import CouncilPeriod


class CouncilPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilPeriod
        fields = [
            'id',
            'period',
            'description',
        ]
