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
    # Lecture : afficher les filières/niveaux détaillés
    filieres = FiliereSerializer(many=True, read_only=True)
    niveaux = NiveauSerializer(many=True, read_only=True)

    # Écriture : permettre d’envoyer juste les IDs pour update
    filieres_ids = serializers.PrimaryKeyRelatedField(
        queryset=Filiere.objects.all(),
        many=True,
        write_only=True,
        required=False
    )
    niveaux_ids = serializers.PrimaryKeyRelatedField(
        queryset=Niveau.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = EtablissementProfile
        fields = [
            "id",
            "nom_etablissement",
            "departement",
            "filieres",
            "niveaux",
            "filieres_ids",
            "niveaux_ids",
            "logo",
        ]


    def update(self, instance, validated_data):
        # Mise à jour des champs simples
        filieres = validated_data.pop("filieres_ids", None)
        niveaux = validated_data.pop("niveaux_ids", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Mise à jour des M2M
        if filieres is not None:
            instance.filieres.set(filieres)
        if niveaux is not None:
            instance.niveaux.set(niveaux)

        return instance

class EtablissProfileLogoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    filieres = FiliereSerializer(many=True, read_only=True)
    niveaux = NiveauSerializer(many=True, read_only=True)

    class Meta:
        model = EtablissementProfile
        fields = [
            "id",
            "nom_etablissement",
            "email",
            "departement",
            "filieres",
            "niveaux",
            "logo",
            "created_at",
        ]
