# importFichier/models.py
from django.db import models
from users.models import EtablissementProfile

class FichierImport(models.Model):
    fichier = models.FileField(upload_to='uploads/')
    nom = models.CharField(max_length=255, blank=True)
    uploaded_by = models.ForeignKey(
        EtablissementProfile,
        on_delete=models.CASCADE,
        related_name="imports"
    )
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom or self.fichier.name


class Departement(models.Model):
    import_file = models.ForeignKey(FichierImport, related_name="departements", on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Centre(models.Model):
    departement = models.ForeignKey(Departement, related_name="centres", on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Filiere(models.Model):
    centre = models.ForeignKey(Centre, related_name="filieres", on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Niveau(models.Model):
    filiere = models.ForeignKey(Filiere, related_name="niveaux", on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
