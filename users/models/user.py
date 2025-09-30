from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from programmes.models import Filiere, Niveau
from .etablissement import EtablissementProfile


# ==================
# Custom Manager
# ==================

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # On force le rôle admin pour les superusers
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# ==================
# Custom User Model
# ==================
class User(AbstractBaseUser, PermissionsMixin):
    prenom = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Le numéro doit être au format : '+999999999'. Jusqu'à 15 chiffres autorisés."
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[phone_validator],
        verbose_name="Téléphone",
        unique=False,  # unicité gérée dans le serializer
    )

    # ✅ Champs ForeignKey corrects
    filiere = models.ForeignKey(
        Filiere,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    etablissement = models.ForeignKey(EtablissementProfile, on_delete=models.CASCADE, related_name="etudiants")  # 👈 obligatoire

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("user", "User"),
        ("etablissement", "Etablissement"),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="user")

    is_online = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["prenom", "nom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}".strip() or self.email

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ["id"]
