from .serialisers import *
from .models import ch_variete
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class ch_varieteAPIView(viewsets.ModelViewSet):
    queryset = ch_variete.objects.all().order_by('VARIETE_ID')
    serializer_class_read=ch_varieteSerializers
    serializer_class_write=insert_ch_varieteSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["ID_FILIERE"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
