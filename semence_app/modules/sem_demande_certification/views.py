from .serialisers import *
from .models import sem_demande_certification
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_demande_certificationAPIView(viewsets.ModelViewSet):
    queryset = sem_demande_certification.objects.all().order_by('DEMANDE_ID')
    serializer_class_read=sem_demande_certificationSerializers
    serializer_class_write=insert_sem_demande_certificationSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["STOCK_ID","STATUT_DEMANDE_CERTIFICATION_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write


    
