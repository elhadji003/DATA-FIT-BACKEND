from rest_framework import generics, permissions
from .models import Candidature, Notification
from .serializers import CandidatureSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CandidatureSerializer, NotificationSerializer
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination



# views.py
class CandidatureCreateView(generics.CreateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        candidature = serializer.save()
        # Créer une notification pour l'établissement concerné
        from .models import Notification
        Notification.objects.create(
            etablissement=candidature.etablissement,
            message=f"Nouvelle candidature reçue de {candidature.nom} {candidature.prenom}"
        )

class CandidatureListView(generics.ListAPIView):
    queryset = Candidature.objects.all().order_by("-date_postule")
    serializer_class = CandidatureSerializer

class CandidatureParEtablissementView(APIView):
    def get(self, request, etab_id):
        candidatures = Candidature.objects.filter(etablissement_id=etab_id).order_by("-date_postule")
        
        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # tu peux changer le nombre par page
        paginated_qs = paginator.paginate_queryset(candidatures, request)

        serializer = CandidatureSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class CandidatureDetailView(generics.RetrieveAPIView):
    queryset = Candidature.objects.all().order_by('id')
    serializer_class = CandidatureSerializer


class CandidatureDeleteView(generics.DestroyAPIView):
    queryset = Candidature.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class CandidatureUpdateStatutView(generics.UpdateAPIView):
    queryset = Candidature.objects.all().order_by('id')
    serializer_class = CandidatureSerializer
    permission_classes = [permissions.IsAuthenticated]  # ou AllowAny si tu veux


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        etab_id = self.kwargs["etab_id"]
        return Notification.objects.filter(etablissement_id=etab_id).order_by("-created_at")
    

# Marquer toutes comme lues
@api_view(["POST"])
def mark_notifications_as_read(request, etab_id):
    notif_qs = Notification.objects.filter(etablissement_id=etab_id, is_read=False)
    updated_count = notif_qs.update(is_read=True)
    return Response({"success": True, "updated": updated_count})