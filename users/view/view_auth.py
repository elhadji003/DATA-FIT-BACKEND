from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from ..models import User
from ..serializers.users_register_serializer import UserRegisterSerializer
from ..serializers.users_login_serializer import MyTokenObtainPairSerializer
from ..serializers.password_serializer import PasswordChangeSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import logout



# ========== Registration View ==========
class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# ========== Login View ==========
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# ========== Logout View ==========
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Déconnecté."})