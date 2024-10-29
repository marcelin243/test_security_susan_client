from .serialisers import *
from user_app.models import acteur_multi_semence
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class acteur_multi_semenceAPIView(viewsets.ModelViewSet):
    queryset = acteur_multi_semence.objects.all().order_by('MULTI_ID')
    serializer_class_read=acteur_multi_semenceSerializers
    serializer_class_write=insert_acteur_multi_semenceSerializers
    
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ["ACTEUR_ID","PROVINCE_ID","COMMUNE_ID","ZONE_ID","UNITE_MESURE_ID","COLLINE_ID"]
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
