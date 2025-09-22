from rest_framework import generics, permissions
from ..models import FichierImport, Departement, Centre, Filiere, Niveau
from ..serializers import (
    DepartementSerializer,
    CentreSerializer,
    FiliereSerializer,
    NiveauSerializer,
    FichierImportSerializer,
)


class ListeImportsView(generics.ListAPIView):
    serializer_class = FichierImportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        etab = self.request.user.etablissement_profile
        return FichierImport.objects.filter(uploaded_by=etab).order_by("-date_upload")


class DepartementsView(generics.ListAPIView):
    serializer_class = DepartementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        etab = self.request.user.etablissement_profile
        import_id = self.kwargs["import_id"]

        # sécurisation : on ne renvoie que si l'import appartient à l'établissement
        return Departement.objects.filter(
            import_file__id=import_id, import_file__uploaded_by=etab
        )


class CentresView(generics.ListAPIView):
    serializer_class = CentreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        etab = self.request.user.etablissement_profile
        departement_id = self.kwargs["departement_id"]

        return Centre.objects.filter(
            departement__id=departement_id,
            departement__import_file__uploaded_by=etab
        )


class FilieresView(generics.ListAPIView):
    serializer_class = FiliereSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        etab = self.request.user.etablissement_profile
        centre_id = self.kwargs["centre_id"]

        return Filiere.objects.filter(
            centre__id=centre_id,
            centre__departement__import_file__uploaded_by=etab
        )


class NiveauxView(generics.ListAPIView):
    serializer_class = NiveauSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        etab = self.request.user.etablissement_profile
        filiere_id = self.kwargs["filiere_id"]

        return Niveau.objects.filter(
            filiere__id=filiere_id,
            filiere__centre__departement__import_file__uploaded_by=etab
        )
