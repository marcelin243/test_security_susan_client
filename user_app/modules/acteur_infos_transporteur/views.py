from user_app.models import acteur_infos_transporteur
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serialisers import *
from django_filters.rest_framework import DjangoFilterBackend


class acteur_infos_transporteurAPIView(viewsets.ModelViewSet):
    queryset = acteur_infos_transporteur.objects.all().order_by('-TRANSPORTEUR_ID')
    serializer_class_read=joint_acteur_infos_transporteurSerializers
    serializer_class_write=insert_acteur_infos_transporteurSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["ACTEUR_ID","TYPE_VEHICULE_ID"] 
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
    