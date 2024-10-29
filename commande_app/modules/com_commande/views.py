
from .serialisers import *
from commande_app.models import com_commande
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class com_commande_APIView(viewsets.ModelViewSet):
    queryset = com_commande.objects.all().order_by('COMMANDE_ID')
    serializer_class_read=jointure_com_commande_Serializers
    serializer_class_write=insert_com_commande_Serializers
    filter_backends = [DjangoFilterBackend]
    
    filterset_fields = ["STATUT_COM_ID","USER_ID"]
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write 