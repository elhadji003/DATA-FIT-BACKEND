# etablissements/models.py
from django.db import models
from django.conf import settings

class EtablissementProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="etablissement_profile"
    )
    nom_etablissement = models.CharField(max_length=150)
    departement = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to="etablissements/logos/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profil Etablissement"
        verbose_name_plural = "Profils Etablissements"
        ordering = ["nom_etablissement"]

    def __str__(self):
        return self.nom_etablissement
