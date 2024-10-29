from .serialisers import sem_commande_semences_statutSerializers
from .models import sem_commande_semences_statut
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_commande_semences_statutAPIView(viewsets.ModelViewSet):
    queryset = sem_commande_semences_statut.objects.all().order_by('STATUT_CMD_DESCR')
    serializer_class=sem_commande_semences_statutSerializers
