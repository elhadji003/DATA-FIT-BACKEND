from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from ..models import Candidature

class StatsFiliereView(APIView):
    """
    Retourne le nombre de candidatures par filière
    """
    def get(self, request):
        # Regroupement par filière, compte des candidatures
        stats = (
            Candidature.objects
            .values("filiere__id", "filiere__nom")
            .annotate(total=Count("id"))
            .order_by("-total")  # Les plus demandées en premier
        )
        return Response(stats)
