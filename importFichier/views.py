from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import FichierImport, Departement, Centre, Filiere, Niveau
import pandas as pd

class UploadFileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        fichier = request.FILES.get("fichier")
        if not fichier:
            return Response({"error": "Aucun fichier envoyé"}, status=status.HTTP_400_BAD_REQUEST)

        # Sauvegarde du fichier
        etablissement = request.user.etablissement_profile
        instance = FichierImport.objects.create(uploaded_by=etablissement ,fichier=fichier, nom=fichier.name)


        # Lecture du fichier
        if fichier.name.endswith(".csv"):
            df = pd.read_csv(instance.fichier.path)
        else:
            df = pd.read_excel(instance.fichier.path)

        # Extraction des données et stockage dans la base
        for dept_name in df["Département"].unique():
            departement = Departement.objects.create(import_file=instance, nom=dept_name)
            centres = df[df["Département"] == dept_name]["Centre"].unique()
            for centre_name in centres:
                centre = Centre.objects.create(departement=departement, nom=centre_name)
                filieres = df[(df["Département"] == dept_name) & (df["Centre"] == centre_name)]["Filiere"].unique()
                for filiere_name in filieres:
                    filiere = Filiere.objects.create(centre=centre, nom=filiere_name)
                    niveaux = df[(df["Département"] == dept_name) & (df["Centre"] == centre_name) & (df["Filiere"] == filiere_name)]["Niveau"].unique()
                    for niveau_name in niveaux:
                        Niveau.objects.create(filiere=filiere, nom=niveau_name)

        return Response({"import_id": instance.id, "nom": instance.nom})
