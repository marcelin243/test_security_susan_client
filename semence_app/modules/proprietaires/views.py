from .serialisers import *
from .models import proprietaires
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class proprietairesAPIView(viewsets.ModelViewSet):
    queryset = proprietaires.objects.all().order_by('NOM_PROPRIETAIRE')
    serializer_class_read=proprietairesSerializers
    serializer_class_write=insert_proprietairesSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["TYPE_PROPRIETAIRE_ID","ID_TYPE_DOCUMENT","CATEGORIE_ID","PROVINCE_ID","COMMUNE_ID","ZONE_ID","COLLINE_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
