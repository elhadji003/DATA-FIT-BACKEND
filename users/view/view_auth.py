from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from ..models import User
from ..serializers.users_register_serializer import UserRegisterSerializer
from ..serializers.users_login_serializer import FastTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import logout


# ========== Registration & User Management ==========
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        # Superadmin peut créer pour n’importe quel établissement (via frontend)
        if user.is_superuser:
            serializer.save()
            return

        # Admin d’établissement → auto-assignation
        if hasattr(user, "etablissement_profile"):
            etab = user.etablissement_profile
            serializer.save(etablissement=etab)
            return

        # Sinon → interdit
        raise PermissionDenied("Vous devez avoir un profil établissement pour créer un étudiant.")

    def get_queryset(self):
        user = self.request.user

        # Superadmin → tous les étudiants
        if user.is_superuser:
            return User.objects.filter(role="user")

        # Admin d’établissement → seulement ses étudiants
        if hasattr(user, "etablissement_profile"):
            return User.objects.filter(role="user", etablissement=user.etablissement_profile)

        # Sinon → rien
        return User.objects.none()


# ========== Login ==========
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = FastTokenObtainPairSerializer


# ========== Logout ==========
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Déconnecté."})
