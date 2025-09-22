from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return JsonResponse({"message": "Bienvenue sur l’API Data-Fit 🚀"})

path('api/imports/', include('importFichier.urls')),

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/programmes/', include('programmes.urls')),
    path('api/fichiers/', include('importFichier.urls')),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
