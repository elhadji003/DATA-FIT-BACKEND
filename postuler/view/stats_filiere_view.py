from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from ..models import Candidature

class StatsFiliereParEtablissementView(APIView):
    """
    Retourne le nombre de candidatures par filière pour l'établissement connecté
    """
    def get(self, request):
        try:
            etab = request.user.etablissement_profile
        except AttributeError:
            return Response({"detail": "Etablissement non trouvé"}, status=404)

        stats = (
            Candidature.objects.filter(etablissement=etab)
            .values("filiere__id", "filiere__nom")
            .annotate(total=Count("id"))
            .order_by("-total")
        )
        return Response({
            "count": stats.count(),
            "results": list(stats)
        })
