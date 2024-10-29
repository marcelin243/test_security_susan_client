"""
URL configuration for sgsf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
router=routers.DefaultRouter()

from user_app.urls import router as user_app_router
# from semence_app.urls import router as semence_app_router
from syst_app.urls import router as syst_app_router
from commande_app.urls import router as commande_app_router


# RECUPERATIONS DE TOUTES LES ROUTES DES APPLICATIONS
#==============================================
router.registry.extend(user_app_router.registry)
# router.registry.extend(semence_app_router.registry)
router.registry.extend(syst_app_router.registry)
router.registry.extend(commande_app_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_app.urls')),
    path('', include('syst_app.urls')),
    path('', include('commande_app.urls')),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

