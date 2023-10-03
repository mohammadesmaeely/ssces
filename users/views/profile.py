from rest_framework import generics

from users.serializers.profile import UserProfileSerializer


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
