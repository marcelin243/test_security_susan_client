from .serialisers import *
from .models import plantation
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class plantationAPIView(viewsets.ModelViewSet):
    queryset = plantation.objects.all().order_by('CODE_PLANTATION')
    serializer_class_read=plantationSerializers
    serializer_class_write=insert_plantationSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["ID_PROPRIETAIRE","PROVINCE_ID","COMMUNE_ID","ZONE_ID","COLLINE_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
