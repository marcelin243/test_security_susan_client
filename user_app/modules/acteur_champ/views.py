from .serialisers import *
from user_app.models import acteur_champ
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class acteur_champAPIView(viewsets.ModelViewSet):
    queryset = acteur_champ.objects.all().order_by('CHAMP_ID')
    serializer_class_read=acteur_champSerializers
    serializer_class_write=insert_acteur_champSerializers
    
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ["ACTEUR_ID","PROVINCE_ID","COMMUNE_ID","ZONE_ID","COLLINE_ID","ID_FILIERE"]
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
