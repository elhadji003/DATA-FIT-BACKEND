# importFichier/urls.py
from django.urls import path
from .views import UploadFileView
from .view.view_getData import ListeImportsView, DepartementsView, CentresView, FilieresView, NiveauxView

urlpatterns = [
    path("upload/", UploadFileView.as_view(), name="upload_file"),
    path("mes-imports/", ListeImportsView.as_view(), name="mes_imports"),
    path("imports/<int:import_id>/departements/", DepartementsView.as_view(), name="departements"),
    path("departements/<int:departement_id>/centres/", CentresView.as_view(), name="centres"),
    path("centres/<int:centre_id>/filieres/", FilieresView.as_view(), name="filieres"),
    path("filieres/<int:filiere_id>/niveaux/", NiveauxView.as_view(), name="niveaux"),
]
