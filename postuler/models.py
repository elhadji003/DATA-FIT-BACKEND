from django.db import models
from users.models import EtablissementProfile
from programmes.models import Filiere, Niveau
from django.utils.timezone import now

class Candidature(models.Model):
    # Relation avec l’établissement
    etablissement = models.ForeignKey(EtablissementProfile, on_delete=models.CASCADE, related_name="candidatures")
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.SET_NULL, null=True)

    # Infos candidat
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    # Infos tuteur
    tuteur_prenom = models.CharField(max_length=100, blank=True, null=True)
    tuteur_nom = models.CharField(max_length=100, blank=True, null=True)
    tuteur_telephone = models.CharField(max_length=20, blank=True, null=True)
    phs = models.BooleanField(default=False)

    # Motivation
    motivation = models.TextField()

    # Statut de la candidature
    STATUS_CHOICES = [
        ("en_attente", "En attente"),
        ("acceptee", "Acceptée"),
        ("rejettee", "Rejetée"),
    ]
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default="en_attente")

    date_postule = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.etablissement.nom_etablissement}"


class Notification(models.Model):
    etablissement = models.ForeignKey(EtablissementProfile, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
 
    def __str__(self):
        return f"Notification pour {getattr(self.etablissement, 'nom_etablissement', 'Établissement inconnu')}"
