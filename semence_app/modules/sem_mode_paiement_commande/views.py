from .serialisers import sem_mode_paiement_commandeSerializers
from .models import sem_mode_paiement_commande
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_mode_paiement_commandeAPIView(viewsets.ModelViewSet):
    queryset = sem_mode_paiement_commande.objects.all().order_by('MODE_PAIEMENT_DESCR')
    serializer_class=sem_mode_paiement_commandeSerializers
