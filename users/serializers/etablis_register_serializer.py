import threading
from django.utils.crypto import get_random_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework import serializers
from ..models import User, EtablissementProfile


class EtablisRegisterSerializer(serializers.ModelSerializer):
    nom_etablissement = serializers.CharField(write_only=True)
    departement = serializers.CharField(write_only=True, required=False)
    logo = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "email", "phone", "avatar",
            "nom_etablissement", "departement", "logo",
        ]

    def create(self, validated_data):
        nom_etablissement = validated_data.pop("nom_etablissement")
        departement = validated_data.pop("departement", None)
        logo = validated_data.pop("logo", None)

        # --- Création utilisateur ---
        random_password = get_random_string(length=12)
        user = User(
            email=validated_data["email"],
            phone=validated_data.get("phone"),
            avatar=validated_data.get("avatar"),
            role="etablissement"
        )
        user.set_password(random_password)
        user.save()

        # --- Création profil établissement ---
        EtablissementProfile.objects.create(
            user=user,
            nom_etablissement=nom_etablissement,
            departement=departement,
            logo=logo
        )

        # --- Email de bienvenue en arrière-plan ---
        threading.Thread(target=self.send_welcome_email, args=(user, random_password)).start()

        return user

    def send_welcome_email(self, user, password):
        subject = "Bienvenue sur la plateforme"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [user.email]

        login_url = "https://votre-domaine.com/login"

        context = {
            "user": user,
            "password": password,
            "login_url": login_url
        }

        text_content = render_to_string("emails/register_etablis.txt", context)
        html_content = render_to_string("emails/register_etablis.html", context)

        email_message = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()
