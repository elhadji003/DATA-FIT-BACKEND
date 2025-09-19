from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return JsonResponse({"message": "Bienvenue sur l’API Data-Fit 🚀"})

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
]
