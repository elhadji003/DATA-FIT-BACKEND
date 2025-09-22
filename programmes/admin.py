from django.contrib import admin
from .models import Filiere, Niveau


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "etablissement")
    list_filter = ("etablissement",)
    search_fields = ("nom",)


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "etablissement")
    list_filter = ("etablissement",)
    search_fields = ("nom",)
