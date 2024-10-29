
from .serialisers import insert_com_commande_statut_Serializers
from commande_app.models import com_commande_statut
from rest_framework import viewsets

class com_commande_statutAPIView(viewsets.ModelViewSet):
    queryset = com_commande_statut.objects.all().order_by('STATUT_COM_DESCR')
    serializer_class = insert_com_commande_statut_Serializers