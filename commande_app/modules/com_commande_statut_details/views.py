
from .serialisers import insert_com_commande_statut_details_Serializers
from commande_app.models import com_commande_statut_details
from rest_framework import viewsets

class com_commande_statut_detailsAPIView(viewsets.ModelViewSet):
    queryset = com_commande_statut_details.objects.all().order_by('COM_STATUT_DET_DESCR')
    serializer_class = insert_com_commande_statut_details_Serializers