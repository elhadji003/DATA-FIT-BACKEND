# programmes/models.py
from django.db import models

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    etablissement = models.ForeignKey(
        "users.EtablissementProfile",
        on_delete=models.CASCADE,
        related_name="filieres"
    )

    class Meta:
        verbose_name = "Filière"
        verbose_name_plural = "Filières"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Niveau(models.Model):
    nom = models.CharField(max_length=50)
    etablissement = models.ForeignKey(
        "users.EtablissementProfile",
        on_delete=models.CASCADE,
        related_name="niveaux"
    )

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"
        ordering = ["nom"]

    def __str__(self):
        return self.nom
