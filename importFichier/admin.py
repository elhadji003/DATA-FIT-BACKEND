# importFichier/admin.py
from django.contrib import admin
from .models import FichierImport

# importFichier/admin.py
@admin.register(FichierImport)
class FichierImportAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fichier', 'date_upload', 'uploaded_by')
    readonly_fields = ('date_upload',)
    list_filter = ('date_upload',)

