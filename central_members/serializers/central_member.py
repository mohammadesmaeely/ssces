from rest_framework import serializers

from central_members.models.central_members import CentralMember


class CentralMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralMember
        fields = [
            'user',
            'name',
            'image',
            'council',
            'phone_number',
            'email',
            'telegram_address',
            'description',
        ]
