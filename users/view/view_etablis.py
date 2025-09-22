from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from ..models import User, EtablissementProfile
from ..serializers.etablis_register_serializer import EtablisRegisterSerializer
from ..serializers.etablis_profile_serializer import EtablissProfileOnlySerializer


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
    # Profile Etablissement
# ===============
class EtablissProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EtablissProfileOnlySerializer

    def get_object(self):
        return EtablissementProfile.objects.get(user=self.request.user)
    

# ===============
# Listes des Etablissement
# ===============
class EtablissementListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = EtablissementProfile.objects.all()
    serializer_class = EtablissProfileOnlySerializer
    pagination_class = EtablissementPagination