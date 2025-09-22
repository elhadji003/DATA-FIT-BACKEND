from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt import serializers
from django.contrib.auth import get_user_model


class FastTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        User = get_user_model()
        error_msg = "Email ou mot de passe incorrect."

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(error_msg)

        if not user.check_password(password):
            raise serializers.ValidationError(error_msg)

        if not user.is_active:
            raise serializers.ValidationError(
                "Votre compte a été désactivé, veuillez contacter l’administrateur."
            )

        # Création du JWT via SimpleJWT
        data = super().validate({
            self.username_field: email,
            'password': password
        })

        # Ajout des infos utilisateur sans bloquer
        data['user'] = {
            'id': user.id,
            'email': user.email,
            'role': user.role,
            'full_name': f"{user.prenom} {user.nom}".strip(),
        }

        return data
