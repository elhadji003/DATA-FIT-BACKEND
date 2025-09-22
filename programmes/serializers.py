from rest_framework import serializers
from .models import Filiere, Niveau

class FiliereSerializer(serializers.ModelSerializer):
    # Affiche le nom de l'établissement directement
    etablissement_nom = serializers.CharField(source='etablissement.nom', read_only=True)
    etablissement = serializers.PrimaryKeyRelatedField(read_only=True) 


    class Meta:
        model = Filiere
        fields = ['id', 'nom', 'etablissement', 'etablissement_nom']

    def validate(self, attrs):
        nom = attrs.get('nom')
        etablissement = attrs.get('etablissement')
        if Filiere.objects.filter(nom=nom, etablissement=etablissement).exists():
            raise serializers.ValidationError("Cette filière existe déjà pour cet établissement.")
        return attrs


class NiveauSerializer(serializers.ModelSerializer):
    # Affiche le nom de l'établissement directement
    etablissement_nom = serializers.CharField(source='etablissement.nom', read_only=True)
    etablissement = serializers.PrimaryKeyRelatedField(read_only=True) 

    class Meta:
        model = Niveau
        fields = ['id', 'nom', 'etablissement', 'etablissement_nom']

    def validate(self, attrs):
        nom = attrs.get('nom')
        etablissement = attrs.get('etablissement')
        if Niveau.objects.filter(nom=nom, etablissement=etablissement).exists():
            raise serializers.ValidationError("Ce niveau existe déjà pour cet établissement.")
        return attrs
