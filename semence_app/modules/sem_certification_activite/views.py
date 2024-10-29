from .serialisers import sem_certification_activiteSerializers
from .models import sem_certification_activite
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_certification_activiteAPIView(viewsets.ModelViewSet):
    queryset = sem_certification_activite.objects.all().order_by('ACTIVITE_DESC')
    serializer_class=sem_certification_activiteSerializers
