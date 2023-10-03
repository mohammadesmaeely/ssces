from rest_framework import serializers

from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'phone_number',
            'student_id',
        ]
        read_only_fields = fields
