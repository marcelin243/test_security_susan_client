
from .serialisers import admin_profilSerializers
from user_app.models import admin_profil
from rest_framework import viewsets

class admin_profilAPIView(viewsets.ModelViewSet):
    queryset = admin_profil.objects.all().order_by('profil_descr')
    serializer_class = admin_profilSerializers