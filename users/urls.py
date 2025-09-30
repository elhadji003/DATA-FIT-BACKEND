from django.urls import path
from .view.view_auth import MyTokenObtainPairView, LogoutView, UserRegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserProfileView, UserUpdateView
from .view.view_password import ChangePasswordView, PasswordResetConfirmView, RequestPasswordResetView
from .view.view_etablis import EtablisRegisterView, EtablissProfileView, EtablissementListView, EtablissementDetailView, EtablissementProfileUpdateView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='auth_register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("profile/update/", UserUpdateView.as_view(), name="user-update"),

    # Etablissement
    path('register/etablissement/', EtablisRegisterView.as_view(), name='auth_register-etablissement'),
    path("profile/etablissement/", EtablissProfileView.as_view(), name="profile-etablissement"),
    path("etablissements/<int:id>/update/", EtablissementProfileUpdateView.as_view(), name="update-etablissement"),
    path("etablissements/listes/", EtablissementListView.as_view(), name="listes-etablissements"),
    path("etablissements/<int:id>/", EtablissementDetailView.as_view(), name="etablissement-detail"),

    # pour les mots de passe
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("forgot-password/", RequestPasswordResetView.as_view(), name="forgot-password"),
    path("reset/password/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="reset-password"),
]