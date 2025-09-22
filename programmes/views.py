# programmes/views.py
from rest_framework import viewsets, permissions
from .models import Filiere, Niveau
from .serializers import FiliereSerializer, NiveauSerializer

class FiliereViewSet(viewsets.ModelViewSet):
    serializer_class = FiliereSerializer
    permission_classes = [permissions.IsAuthenticated]  # ou custom si besoin

    def get_queryset(self):
        # Récupère uniquement les filières du profil de l'utilisateur connecté
        etab = self.request.user.etablissement_profile
        return Filiere.objects.filter(etablissement=etab)

    def perform_create(self, serializer):
        serializer.save(etablissement=self.request.user.etablissement_profile)


class NiveauViewSet(viewsets.ModelViewSet):
    serializer_class = NiveauSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        etab = self.request.user.etablissement_profile
        return Niveau.objects.filter(etablissement=etab)

    def perform_create(self, serializer):
        serializer.save(etablissement=self.request.user.etablissement_profile)
