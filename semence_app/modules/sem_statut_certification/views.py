from .serialisers import sem_statut_certificationSerializers
from .models import sem_statut_certification
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_statut_certificationAPIView(viewsets.ModelViewSet):
    queryset = sem_statut_certification.objects.all().order_by('STATUT_DEMANDE_CERTIFICATION_DESCR')
    serializer_class=sem_statut_certificationSerializers
