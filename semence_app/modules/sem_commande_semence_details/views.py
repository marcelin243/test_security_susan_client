from .serialisers import *
from .models import sem_commande_semence_details
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_commande_semence_detailsAPIView(viewsets.ModelViewSet):
    queryset = sem_commande_semence_details.objects.all().order_by('ID_RELATION_COM')
    serializer_class_read=sem_commande_semence_detailsSerializers
    serializer_class_write=insert_sem_commande_semence_detailsSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["STOCK_ID","COMMANDE_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
