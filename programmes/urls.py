from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FiliereViewSet, NiveauViewSet

router = DefaultRouter()
router.register(r'filieres', FiliereViewSet, basename="filieres")
router.register(r'niveaux', NiveauViewSet, basename="niveaux")

urlpatterns = [
    path("", include(router.urls)),
]
