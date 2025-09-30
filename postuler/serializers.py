from rest_framework import serializers
from .models import Candidature, Notification

class CandidatureSerializer(serializers.ModelSerializer):
    filiereNom = serializers.CharField(source="filiere.nom", read_only=True)
    niveauNom = serializers.CharField(source="niveau.nom", read_only=True)
    etablissementNom = serializers.CharField(source="etablissement.nom_etablissement", read_only=True)

    class Meta:
        model = Candidature
        fields = "__all__"
        read_only_fields = ["id", "date_postule", "statut", "filiereNom", "niveauNom", "etablissementNom"]
    

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
