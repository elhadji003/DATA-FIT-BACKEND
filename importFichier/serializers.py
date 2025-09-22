from rest_framework import serializers
from .models import FichierImport, Departement, Centre, Filiere, Niveau

class FichierImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichierImport
        fields = "__all__"

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = "__all__"

class CentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centre
        fields = "__all__"

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = "__all__"
