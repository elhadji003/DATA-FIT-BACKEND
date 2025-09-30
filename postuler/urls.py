# postuler/urls.py
from django.urls import path
from .views import (
    CandidatureListView,
    CandidatureParEtablissementView,
    CandidatureDetailView,
    CandidatureCreateView,
    CandidatureDeleteView,
    CandidatureUpdateStatutView,
    NotificationListView,
    mark_notifications_as_read
)
from .view.stats_filiere_view import StatsFiliereParEtablissementView

urlpatterns = [
    path("candidatures/", CandidatureListView.as_view(), name="liste-candidatures"),
    path("candidatures/postuler/", CandidatureCreateView.as_view(), name="postuler"),
    path("candidatures/<int:pk>/", CandidatureDetailView.as_view(), name="detail-candidature"),
    path("candidatures/<int:id>/delete/", CandidatureDeleteView.as_view(), name="candidature-delete"),
    path("candidatures/etablissement/<int:etab_id>/", CandidatureParEtablissementView.as_view(), 
    name="candidatures-par-etablissement"),
    path('candidatures/<int:pk>/update-statut/', CandidatureUpdateStatutView.as_view(), 
    name='candidature-update-statut'),
    path("notifications/<int:etab_id>/", NotificationListView.as_view(), name="liste-notifs"),
    path("notifications/<int:etab_id>/mark-as-read/", mark_notifications_as_read, name="notif-mark-read"),
    path("stats/filiere/",StatsFiliereParEtablissementView.as_view(), name="stats-filiere"),

]
