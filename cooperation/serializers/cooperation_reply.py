from rest_framework import serializers

from cooperation.models.cooperation_reply import CooperationReply
from cooperation.serializers.cooperation_form import CooperationFormSerializer


class CooperationReplySerializer(serializers.ModelSerializer):
    cooperation_detail = CooperationFormSerializer(source='cooperation', read_only=True)
    class Meta:
        model = CooperationReply
        fields = [
            'cooperation',
            'cooperation_detail',
            'text',
            'phone_number',
            'email',
        ]
