from .serialisers import *
from .models import sem_stock_semence
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_stock_semenceAPIView(viewsets.ModelViewSet):
    queryset = sem_stock_semence.objects.all().order_by('STOCK_ID')
    serializer_class_read=sem_stock_semenceSerializers
    serializer_class_write=insert_sem_stock_semenceSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["FILIERE_ID","ID_PROPRIETAIRE"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
