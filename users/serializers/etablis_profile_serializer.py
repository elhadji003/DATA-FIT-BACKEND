from rest_framework import serializers
from ..models import EtablissementProfile
from programmes.models import Filiere, Niveau


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ["id", "nom"]


class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ["id", "nom"]

class EtablissProfileOnlySerializer(serializers.ModelSerializer):
    filieres = FiliereSerializer(many=True, read_only=True, source="programmes.filieres")
    niveaux = NiveauSerializer(many=True, read_only=True, source="programmes.niveaux")
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = EtablissementProfile
        fields = [
            "id",
            "nom_etablissement",
            "departement",
            "filieres",
            "niveaux",
            "logo_url",
        ]
        read_only_fields = fields

    def get_logo_url(self, obj):
        request = self.context.get("request")
        if obj.logo and request:
            return request.build_absolute_uri(obj.logo.url)
        elif obj.logo:
            return obj.logo.url
        return None
