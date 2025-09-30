from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from ..models import User
import threading


class UserRegisterSerializer(serializers.ModelSerializer):
    filiere_nom = serializers.SerializerMethodField()
    niveau_nom = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", "prenom", "nom", "email", "phone",
            "filiere", "filiere_nom",
            "niveau", "niveau_nom",
            "etablissement"
        ]

    def get_filiere_nom(self, obj):
        return obj.filiere.nom if obj.filiere else None

    def get_niveau_nom(self, obj):
        return obj.niveau.nom if obj.niveau else None

    def validate(self, data):
        email = data.get("email")
        phone = data.get("phone")

        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Cet email est déjà utilisé."})
        if phone and User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError({"phone": "Ce numéro de téléphone est déjà utilisé."})
        return data

    def create(self, validated_data):
        random_password = get_random_string(length=12)

        user = User.objects.create_user(
            role="user",
            password=random_password,
            **validated_data
        )

        threading.Thread(target=self.send_welcome_email, args=(user, random_password)).start()
        return user

    def send_welcome_email(self, user, password):
        subject = "Bienvenue sur la plateforme"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [user.email]

        login_url = "https://data-fit-frontend.vercel.app/login/"

        context = {
            "user": user,
            "password": password,
            "login_url": login_url
        }

        text_content = render_to_string("emails/register_user.txt", context)
        html_content = render_to_string("emails/register_user.html", context)

        email_message = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()
