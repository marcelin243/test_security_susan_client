from .serialisers import *
from user_app.models import acteur_infos
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend as FB

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class acteur_infosAPIView(viewsets.ModelViewSet):
    queryset = acteur_infos.objects.all().order_by('NOM')
    serializer_class_read=acteur_infosSerializers
    serializer_class_write=insert_acteur_infosSerializers
    filter_backends = [FB] 
    filterset_fields = ["STATUT_JURIDIQUE_ID","PROFIL_ID","PROVINCE_ID","COMMUNE_ID","ZONE_ID","COLLINE_ID"]

    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write