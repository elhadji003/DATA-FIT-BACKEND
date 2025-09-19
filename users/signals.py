from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


# =========================
# Quand l'utilisateur se connecte
# =========================
@receiver(user_logged_in)
def set_user_online(sender, request, user, **kwargs):
    user.is_online = True
    user.last_login = timezone.now()  # met à jour la dernière connexion
    user.save(update_fields=["is_online", "last_login"])


# =========================
# Quand l'utilisateur se déconnecte
# =========================
@receiver(user_logged_out)
def set_user_offline(sender, request, user, **kwargs):
    if user:
        user.is_online = False
        user.save(update_fields=["is_online"])
