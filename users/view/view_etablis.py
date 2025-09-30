from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from ..models import User, EtablissementProfile
from ..serializers.etablis_register_serializer import EtablisRegisterSerializer
from ..serializers.etablis_profile_serializer import EtablissProfileOnlySerializer, EtablissProfileLogoSerializer


# ==================
    # Pagination
# ==================
class EtablissementPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# ===============
    # Register Etablissement
# ===============
class EtablisRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = EtablisRegisterSerializer

# ===============
# Listes des Etablissement
# ===============
class EtablissementListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = EtablissementProfile.objects.all()
    serializer_class = EtablissProfileOnlySerializer
    pagination_class = EtablissementPagination

# ================
# Etablissement ID
# ================
class EtablissementDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]  # ou IsAuthenticated si nécessaire
    queryset = EtablissementProfile.objects.all()
    serializer_class = EtablissProfileOnlySerializer
    lookup_field = "id"


# =================================
# Modifiier le Profile Etablissement
# =================================
class EtablissementProfileView(generics.RetrieveUpdateAPIView):
    """
    GET: Récupère les infos de l'établissement connecté
    PATCH/PUT: Met à jour le nom, département et logo
    """
    serializer_class = EtablissProfileLogoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # On retourne le profile lié à l'utilisateur connecté
        return EtablissementProfile.objects.get(user=self.request.user)