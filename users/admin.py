from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Infos personnelles", {"fields": ("prenom", "nom", "phone", "nom_etablissement", "avatar")}),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login", "created_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "prenom", "nom", "phone", "password1", "password2"),
        }),
    )
    list_display = ("id", "email", "prenom", "nom", "role", "is_active")
    search_fields = ("email", "prenom", "nom", "phone")
    ordering = ("id",)
