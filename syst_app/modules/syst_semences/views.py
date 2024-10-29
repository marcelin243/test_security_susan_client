from .serialisers import *
from syst_app.models import syst_semences
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#  VIEWS POUR SYST SEMENCE
#===============================
class syst_semencesAPIView(viewsets.ModelViewSet):
    queryset = syst_semences.objects.all().order_by('SEMENCE_DESCR')
    serializer_class_read=syst_semencesSerializers
    serializer_class_write=insert_syst_semencesSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["TYPE_SEMENCE_ID","ID_CAT_SEMENCE"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
