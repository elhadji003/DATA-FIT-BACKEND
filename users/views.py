from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers.user_profile_serializer import UserProfileSerializer, UserUpdateSerializer

User = get_user_model()


# ==================
# Voir son profil
# ==================
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# ==================
# Mettre à jour son profil
# ==================
class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
