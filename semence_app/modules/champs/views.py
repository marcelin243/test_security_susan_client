from .serialisers import *
from .models import champs
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class champsAPIView(viewsets.ModelViewSet):
    queryset = champs.objects.all().order_by('DESCR_CHAMP')
    serializer_class_read=champsSerializers
    serializer_class_write=insert_champsSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["USER_ID","ID_PLANTATION","PROVINCE_ID","COMMUNE_ID","ZONE_ID","COLLINE_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
