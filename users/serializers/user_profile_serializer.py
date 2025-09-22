from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# ======================
# Serializer pour le profil
# ======================
class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "prenom",
            "nom",
            "full_name",
            "phone",
            "role",
            "avatar",
            "is_online",
            "created_at",
        ]
        read_only_fields = ["id", "email", "role", "is_online", "created_at"]

    def get_full_name(self, obj):
        return f"{obj.prenom or ''} {obj.nom or ''}".strip() or obj.email


# ======================
# Serializer pour mise à jour
# ======================
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "prenom",
            "nom",
            "phone",
            "avatar",
        ]
